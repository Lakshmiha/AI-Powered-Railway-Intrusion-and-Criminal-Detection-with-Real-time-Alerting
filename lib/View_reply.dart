// import 'dart:convert';
//
// import 'package:flutter/material.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
//
// import 'newhome.dart';
//
// void main() {
//   runApp(const view_reply(title: null,));
// }
//
// class view_reply extends StatelessWidget {
//   final dynamic title;
//
//   const view_reply({super.key, required this.title});
//
//   @override
//   Widget build(BuildContext context) {
//     return const MaterialApp(
//       home: view_replies(title: 'View Users'),
//     );
//   }
// }
//
// class view_replies extends StatefulWidget {
//   const view_replies({super.key, required this.title});
//   final String title;
//
//   @override
//   State<view_replies> createState() => _view_repliesState();
// }
//
// class _view_repliesState extends State<view_replies> {
//   List<Map<String, dynamic>> users = [];
//   List<Map<String, dynamic>> filteredUsers = [];
//   List<String> nameSuggestions = [];
//
//   @override
//   void initState() {
//     super.initState();
//     viewUsers("");
//   }
//
//   Future<void> viewUsers(String searchValue) async {
//     try {
//       SharedPreferences sh = await SharedPreferences.getInstance();
//       String urls = sh.getString('url') ?? '';
//       String img = sh.getString('img_url') ?? '';
//       String lid = sh.getString('lid') ?? '';
//       String apiUrl = '$urls/app_viewreply_get/';
//
//       var response = await http.post(Uri.parse(apiUrl), body: {
//         'lid':lid
//       });
//       var jsonData = json.decode(response.body);
//
//       if (jsonData['status'] == 'ok') {
//         List<Map<String, dynamic>> tempList = [];
//         for (var item in jsonData['data']) {
//           tempList.add({
//             'id': item['id'],
//             'date': item['date'],
//             'complaint': item['complaint'],
//             'reply': item['reply'],
//             'status': item['status'],
//           });
//         }
//         setState(() {
//           users = tempList;
//           filteredUsers = tempList
//               .where((user) =>
//               user['name']
//                   .toString()
//                   .toLowerCase()
//                   .contains(searchValue.toLowerCase()))
//               .toList();
//           nameSuggestions = users.map((e) => e['name'].toString()).toSet().toList();
//         });
//       }
//     } catch (e) {
//       print("Error fetching users: $e");
//     }
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return WillPopScope(
//         onWillPop: () async {
//       Navigator.pushReplacement(
//         context,
//         MaterialPageRoute(builder: (context) => const HomePage()),
//       );
//       return false; // Prevent default pop
//     },
//     child:Scaffold(
//       appBar: AppBar(
//         backgroundColor: Color.fromARGB(255, 232, 177, 61),
//         title: Text('Search by name'),
//         // suggestions: nameSuggestions,
//         // onSearch: (value) {
//         //   setState(() {
//         //     filteredUsers = users
//         //         .where((user) => user['name']
//         //         .toString()
//         //         .toLowerCase()
//         //         .contains(value.toLowerCase()))
//         //         .toList();
//         //   });
//         // },
//       ),
//       body: ListView.builder(
//         shrinkWrap: true,
//         physics: BouncingScrollPhysics(),
//         itemCount: filteredUsers.length,
//         itemBuilder: (context, index) {
//           final user = filteredUsers[index];
//           return Card(
//             margin: const EdgeInsets.all(10),
//             elevation: 5,
//             child: ListTile(
//               // leading: CircleAvatar(
//               //   backgroundImage: NetworkImage(user['photo']),
//               //   radius: 30,
//               // ),
//               // title: Text(user['name'], style: TextStyle(fontWeight: FontWeight.bold)),
//               subtitle: Column(
//                 crossAxisAlignment: CrossAxisAlignment.start,
//                 children: [
//                   Text("Date: ${user['date']}"),
//                   Text("Complaint: ${user['complaint']}"),
//                   Text("Reply: ${user['reply']}"),
//                   Text("Status: ${user['status']}"),
//                 ],
//               ),
//             ),
//           );
//         },
//       ),
//     ));
//   }
// }
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'newhome.dart'; // your home page

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ViewRepliesPage(),
  ));
}

class ViewRepliesPage extends StatefulWidget {
  const ViewRepliesPage({super.key});

  @override
  State<ViewRepliesPage> createState() => _ViewRepliesPageState();
}

class _ViewRepliesPageState extends State<ViewRepliesPage> {
  List<Map<String, dynamic>> _replies = [];
  List<Map<String, dynamic>> _filteredReplies = [];
  final _searchController = TextEditingController();
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchReplies();
    _searchController.addListener(_filterReplies);
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _fetchReplies() async {
    setState(() => _isLoading = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? '';
      final lid = sh.getString('lid') ?? '';

      if (baseUrl.isEmpty || lid.isEmpty) {
        Fluttertoast.showToast(msg: "Missing configuration");
        return;
      }

      final uri = Uri.parse('$baseUrl/app_viewreply_get/');
      final res = await http.post(uri, body: {'lid': lid});

      if (res.statusCode == 200) {
        final data = json.decode(res.body);
        if (data['status'] == 'ok') {
          final List<Map<String, dynamic>> items = (data['data'] as List).map((item) {
            return {
              'id': item['id']?.toString() ?? '',
              'date': item['date']?.toString() ?? 'N/A',
              'complaint': item['complaint']?.toString() ?? '',
              'reply': item['reply']?.toString() ?? 'No reply yet',
              'status': (item['status']?.toString() ?? 'pending').toLowerCase(),
            };
          }).toList();

          setState(() {
            _replies = items;
            _filteredReplies = items;
          });
        } else {
          Fluttertoast.showToast(msg: "No data found");
        }
      } else {
        Fluttertoast.showToast(msg: "Server error");
      }
    } catch (e) {
      Fluttertoast.showToast(msg: "Error: $e");
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  void _filterReplies() {
    final query = _searchController.text.trim().toLowerCase();
    setState(() {
      _filteredReplies = _replies.where((item) {
        // Search in complaint or reply (you can add more fields)
        return item['complaint'].toLowerCase().contains(query) ||
            item['reply'].toLowerCase().contains(query);
      }).toList();
    });
  }

  Color _getStatusColor(String status) {
    switch (status) {
      case 'replied':
      case 'resolved':
        return Colors.green.shade700;
      case 'pending':
        return Colors.orange.shade800;
      case 'rejected':
        return Colors.red.shade700;
      default:
        return Colors.grey.shade700;
    }
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (_) => const HomePage()),
        );
        return false;
      },
      child: Scaffold(
        backgroundColor: const Color(0xFFF5F7FA),
        appBar: AppBar(
          elevation: 0,
          backgroundColor: Colors.white,
          foregroundColor: Colors.black87,
          title: const Text("My Complaints & Replies"),
          actions: [
            IconButton(
              icon: const Icon(Icons.refresh_rounded),
              onPressed: _fetchReplies,
            ),
          ],
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(56),
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
              child: TextField(
                controller: _searchController,
                decoration: InputDecoration(
                  hintText: "Search complaints or replies...",
                  prefixIcon: const Icon(Icons.search_rounded),
                  filled: true,
                  fillColor: Colors.grey.shade100,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(30),
                    borderSide: BorderSide.none,
                  ),
                  contentPadding: const EdgeInsets.symmetric(vertical: 0),
                ),
              ),
            ),
          ),
        ),
        body: RefreshIndicator(
          onRefresh: _fetchReplies,
          child: _isLoading
              ? const Center(child: CircularProgressIndicator())
              : _filteredReplies.isEmpty
              ? _buildEmptyState()
              : ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _filteredReplies.length,
            itemBuilder: (context, index) {
              final item = _filteredReplies[index];
              return _buildReplyCard(item);
            },
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.inbox_outlined, size: 80, color: Colors.grey.shade400),
          const SizedBox(height: 16),
          Text(
            "No replies found",
            style: TextStyle(fontSize: 20, color: Colors.grey.shade700),
          ),
          const SizedBox(height: 8),
          Text(
            "Pull down to refresh or submit a new complaint",
            style: TextStyle(color: Colors.grey.shade500),
          ),
        ],
      ),
    );
  }

  Widget _buildReplyCard(Map<String, dynamic> item) {
    final status = item['status'] as String;
    final statusColor = _getStatusColor(status);

    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header row: Date + Status badge
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  item['date'],
                  style: TextStyle(
                    fontSize: 13,
                    color: Colors.grey.shade600,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                Badge(
                  label: Text(
                    status.toUpperCase(),
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  backgroundColor: statusColor,
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 2),
                  largeSize: 22,
                ),
              ],
            ),

            const SizedBox(height: 12),

            // Complaint
            const Text(
              "Complaint",
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 15,
                color: Color(0xFF1A237E),
              ),
            ),
            const SizedBox(height: 4),
            Text(
              item['complaint'],
              style: const TextStyle(height: 1.4),
            ),

            const SizedBox(height: 16),
            const Divider(height: 1),

            const SizedBox(height: 16),

            // Reply
            const Text(
              "Admin Reply",
              style: TextStyle(
                fontWeight: FontWeight.w600,
                fontSize: 15,
                color: Color(0xFF1A237E),
              ),
            ),
            const SizedBox(height: 4),
            Text(
              item['reply'],
              style: TextStyle(
                color: status == 'pending' ? Colors.grey.shade700 : Colors.black87,
                height: 1.4,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
