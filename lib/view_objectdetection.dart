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
//       home: viewobjdetection(title: 'View Users'),
//     );
//   }
// }
//
// class viewobjdetection extends StatefulWidget {
//   const viewobjdetection({super.key, required this.title});
//   final String title;
//
//   @override
//   State<viewobjdetection> createState() => _viewobjdetectionState();
// }
//
// class _viewobjdetectionState extends State<viewobjdetection> {
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
//       String apiUrl = '$urls/app_viewobjectdetectionpolice_get/';
//
//       var response = await http.post(Uri.parse(apiUrl), body: {});
//       var jsonData = json.decode(response.body);
//
//       if (jsonData['status'] == 'ok') {
//         List<Map<String, dynamic>> tempList = [];
//         for (var item in jsonData['data']) {
//           tempList.add({
//             'id': item['id'],
//             'log': img+item['log'],
//             'place': item['place'],
//             'time': item['time'],
//             'date': item['date'],
//           });
//         }
//         setState(() {
//           users = tempList;
//           filteredUsers = tempList
//               .where((user) =>
//               user['place']
//                   .toString()
//                   .toLowerCase()
//                   .contains(searchValue.toLowerCase()))
//               .toList();
//           nameSuggestions = users.map((e) => e['place'].toString()).toSet().toList();
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
//       // appBar: EasySearchBar(
//       //   backgroundColor: Color.fromARGB(255, 232, 177, 61),
//       //   title: Text('Search by name'),
//       //   suggestions: nameSuggestions,
//       //   onSearch: (value) {
//       //     setState(() {
//       //       filteredUsers = users
//       //           .where((user) => user['name']
//       //           .toString()
//       //           .toLowerCase()
//       //           .contains(value.toLowerCase()))
//       //           .toList();
//       //     });
//       //   },
//       // ),
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
//               //   backgroundImage: NetworkImage(),
//               //   radius: 30,
//               // ),
//               title: Text(user['place'], style: TextStyle(fontWeight: FontWeight.bold)),
//               subtitle: Column(
//                 crossAxisAlignment: CrossAxisAlignment.start,
//                 children: [
//                   Image.network(user['log'],height: 100,width: 100,),
//                   Text("Place: ${user['place']}"),
//                   Text("Time: ${user['time']}"),
//                   Text("Date: ${user['date']}"),
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

import 'newhome.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ViewObjectsDetectionPage(),
  ));
}

class ViewObjectsDetectionPage extends StatefulWidget {
  const ViewObjectsDetectionPage({super.key});

  @override
  State<ViewObjectsDetectionPage> createState() => _ViewObjectsDetectionPageState();
}

class _ViewObjectsDetectionPageState extends State<ViewObjectsDetectionPage> {
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

      final uri = Uri.parse('$baseUrl/app_viewobjectdetectionpolice_get/');
      final res = await http.post(uri, body: {});

      if (res.statusCode == 200) {
        final data = json.decode(res.body);
        if (data['status'] == 'ok') {
          final List items = (data['data'] as List?) ?? [];
          final temp = items.map((e) {
            return {
              'id': e['id']?.toString() ?? '',
              'log': imgBase + (e['log']?.toString() ?? ''),
              'place': e['place']?.toString() ?? 'Unknown',
              'time': e['time']?.toString() ?? 'N/A',
              'date': e['date']?.toString() ?? 'N/A',
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
        return item['place'].toLowerCase().contains(query) ||
            item['date'].toLowerCase().contains(query);
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
          title: const Text("Objects Detected"),
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
                  hintText: "Search by place or date...",
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
              return _buildObjectCard(_filteredItems[index]);
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
          Icon(Icons.hide_image_outlined, size: 80, color: Colors.grey.shade400),
          const SizedBox(height: 16),
          const Text("No objects detected yet", style: TextStyle(fontSize: 18, color: Colors.grey)),
          const SizedBox(height: 8),
          Text("Pull down to refresh", style: TextStyle(color: Colors.grey.shade500)),
        ],
      ),
    );
  }

  Widget _buildObjectCard(Map<String, dynamic> item) {
    final imgUrl = item['log'] as String;

    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Image
          AspectRatio(
            aspectRatio: 16 / 9,
            child: Image.network(
              imgUrl,
              fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Container(
                color: Colors.grey.shade200,
                child: const Center(child: Icon(Icons.broken_image, size: 60, color: Colors.grey)),
              ),
              loadingBuilder: (_, child, progress) {
                if (progress == null) return child;
                return const Center(child: CircularProgressIndicator(strokeWidth: 2));
              },
            ),
          ),

          Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Badge(
                      label: Text(
                        "Detected",
                        style: const TextStyle(fontSize: 11, color: Colors.white),
                      ),
                      backgroundColor: Colors.teal.shade700,
                      padding: const EdgeInsets.symmetric(horizontal: 10),
                    ),
                    const Spacer(),
                    Text(
                      "${item['date']} • ${item['time']}",
                      style: TextStyle(fontSize: 13, color: Colors.grey.shade700),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                Text(
                  item['place'],
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w600,
                    color: Color(0xFF1A237E),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
