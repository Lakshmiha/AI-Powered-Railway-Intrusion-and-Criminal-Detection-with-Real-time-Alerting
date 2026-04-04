// import 'dart:convert';
//
// import 'package:flutter/material.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
//
// import 'newhome.dart';
//
// void main() {
//   runApp(const ViewHouseApp());
// }
//
// class ViewHouseApp extends StatelessWidget {
//   const ViewHouseApp({Key? key}) : super(key: key);
//
//   @override
//   Widget build(BuildContext context) {
//     return const MaterialApp(
//       home: viewcrimdetection(title: 'View Users'),
//     );
//   }
// }
//
// class viewcrimdetection extends StatefulWidget {
//   const viewcrimdetection({super.key, required this.title});
//   final String title;
//
//   @override
//   State<viewcrimdetection> createState() => _viewcrimdetectionState();
// }
//
// class _viewcrimdetectionState extends State<viewcrimdetection> {
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
//       String apiUrl = '$urls/app_viewcriminaldetectionpolice_get/';
//
//       var response = await http.post(Uri.parse(apiUrl), body: {});
//       var jsonData = json.decode(response.body);
//
//       if (jsonData['status'] == 'ok') {
//         List<Map<String, dynamic>> tempList = [];
//         for (var item in jsonData['data']) {
//           tempList.add({
//             'id': item['id'],
//             'date': item['date'],
//             'photo': img+item['photo'],
//             'time': item['time'],
//           });
//         }
//         setState(() {
//           users = tempList;
//           filteredUsers = tempList;
//           //     .where((user) =>
//           //     user['place']
//           //         .toString()
//           //         .toLowerCase()
//           //         .contains(searchValue.toLowerCase()))
//           //     .toList();
//           // nameSuggestions = users.map((e) => e['place'].toString()).toSet().toList();
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
//           Navigator.pushReplacement(
//             context,
//             MaterialPageRoute(builder: (context) => const HomePage()),
//           );
//           return false; // Prevent default pop
//         },
//         child:Scaffold(
//           // appBar: EasySearchBar(
//           //   backgroundColor: Color.fromARGB(255, 232, 177, 61),
//           //   title: Text('Search by name'),
//           //   suggestions: nameSuggestions,
//           //   onSearch: (value) {
//           //     setState(() {
//           //       filteredUsers = users
//           //           .where((user) => user['name']
//           //           .toString()
//           //           .toLowerCase()
//           //           .contains(value.toLowerCase()))
//           //           .toList();
//           //     });
//           //   },
//           // ),
//           body: ListView.builder(
//             shrinkWrap: true,
//             physics: BouncingScrollPhysics(),
//             itemCount: filteredUsers.length,
//             itemBuilder: (context, index) {
//               final user = filteredUsers[index];
//               return Card(
//                 margin: const EdgeInsets.all(10),
//                 elevation: 5,
//                 child: ListTile(
//                   // leading: CircleAvatar(
//                   //   backgroundImage: NetworkImage(),
//                   //   radius: 30,
//                   // ),
//                   // title: Text(user['place'], style: TextStyle(fontWeight: FontWeight.bold)),
//                   subtitle: Column(
//                     crossAxisAlignment: CrossAxisAlignment.start,
//                     children: [
//                       Text("Date: ${user['date']}"),
//                       Image.network(user['photo'],height: 100,width: 100,),
//                       Text("Time: ${user['time']}"),
//                     ],
//                   ),
//                 ),
//               );
//             },
//           ),
//         ));
//   }
// }
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'newhome.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ViewCriminalsDetectionPage(),
  ));
}

class ViewCriminalsDetectionPage extends StatefulWidget {
  const ViewCriminalsDetectionPage({super.key});

  @override
  State<ViewCriminalsDetectionPage> createState() => _ViewCriminalsDetectionPageState();
}

class _ViewCriminalsDetectionPageState extends State<ViewCriminalsDetectionPage> {
  List<Map<String, dynamic>> _items = [];
  List<Map<String, dynamic>> _filteredItems = [];
  final _searchController = TextEditingController();
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchData();
    _searchController.addListener(_applyFilter);
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _fetchData() async {
    setState(() => _isLoading = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? '';
      final imgBase = sh.getString('img_url') ?? '';

      if (baseUrl.isEmpty) return;

      final uri = Uri.parse('$baseUrl/app_viewcriminaldetectionpolice_get/');
      final res = await http.post(uri, body: {});

      if (res.statusCode == 200) {
        final data = json.decode(res.body);
        if (data['status'] == 'ok') {
          final List items = (data['data'] as List?) ?? [];
          final temp = items.map((e) {
            return {
              'id': e['id']?.toString() ?? '',
              'photo': imgBase + (e['photo']?.toString() ?? ''),
              'date': e['date']?.toString() ?? 'N/A',
              'time': e['time']?.toString() ?? 'N/A',
            };
          }).toList();

          setState(() {
            _items = temp.cast<Map<String, dynamic>>();
            _filteredItems = temp.cast<Map<String, dynamic>>();
          });
        }
      }
    } catch (e) {
      debugPrint("Fetch error: $e");
      Fluttertoast.showToast(msg: "Failed to load data");
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  void _applyFilter() {
    final query = _searchController.text.trim().toLowerCase();
    setState(() {
      _filteredItems = _items.where((item) {
        return item['date'].toLowerCase().contains(query);
      }).toList();
    });
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
          title: const Text("Criminals Detected"),
          actions: [
            IconButton(
              icon: const Icon(Icons.refresh_rounded),
              onPressed: _fetchData,
            ),
          ],
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(56),
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
              child: TextField(
                controller: _searchController,
                decoration: InputDecoration(
                  hintText: "Search by date...",
                  prefixIcon: const Icon(Icons.search),
                  filled: true,
                  fillColor: Colors.grey.shade100,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(30),
                    borderSide: BorderSide.none,
                  ),
                ),
              ),
            ),
          ),
        ),
        body: RefreshIndicator(
          onRefresh: _fetchData,
          child: _isLoading
              ? const Center(child: CircularProgressIndicator())
              : _filteredItems.isEmpty
              ? _buildEmptyState()
              : ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _filteredItems.length,
            itemBuilder: (context, index) {
              return _buildCriminalCard(_filteredItems[index]);
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
          Icon(Icons.no_accounts_outlined, size: 80, color: Colors.grey.shade400),
          const SizedBox(height: 16),
          const Text("No detections recorded", style: TextStyle(fontSize: 18, color: Colors.grey)),
          const SizedBox(height: 8),
          Text("Pull down to refresh", style: TextStyle(color: Colors.grey.shade500)),
        ],
      ),
    );
  }

  Widget _buildCriminalCard(Map<String, dynamic> item) {
    final imgUrl = item['photo'] as String;

    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Photo
          AspectRatio(
            aspectRatio: 3 / 4,
            child: Image.network(
              imgUrl,
              fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Container(
                color: Colors.grey.shade200,
                child: const Center(child: Icon(Icons.person_off, size: 60, color: Colors.grey)),
              ),
              loadingBuilder: (_, child, progress) {
                if (progress == null) return child;
                return const Center(child: CircularProgressIndicator(strokeWidth: 2));
              },
            ),
          ),

          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Badge(
                  label: Text(
                    "FLAGGED",
                    style: const TextStyle(fontSize: 11, color: Colors.white),
                  ),
                  backgroundColor: Colors.red.shade700,
                  padding: const EdgeInsets.symmetric(horizontal: 12),
                ),
                Text(
                  "${item['date']} • ${item['time']}",
                  style: TextStyle(fontSize: 13, color: Colors.grey.shade700),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
