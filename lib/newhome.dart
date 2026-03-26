// import 'dart:async';
// import 'dart:convert';
//
// import 'package:flutter/material.dart';
// import 'package:railway/View_reply.dart';
// import 'package:railway/send_complaint.dart';
// import 'package:railway/view_criminaldetection.dart';
// import 'package:railway/view_objectdetection.dart';
// import 'package:railway/viewprofile.dart';
//
// import 'Change_password.dart';
// import 'package:flutter_local_notifications/flutter_local_notifications.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
//
//
// void main() {
//   runApp(const MaterialApp(
//     debugShowCheckedModeBanner: false,
//     home: home_page(),
//   ));
// }
//
// void callbackDispatcher(String message) {
//   FlutterLocalNotificationsPlugin flip = FlutterLocalNotificationsPlugin();
//   var android = new AndroidInitializationSettings('@mipmap/ic_launcher');
//   var settings = new InitializationSettings(android: android);
//   flip.initialize(settings);
//   _showNotificationWithDefaultSound(flip, message);
// }
//
// Future _showNotificationWithDefaultSound(
//     FlutterLocalNotificationsPlugin flip, String message) async {
//   var androidPlatformChannelSpecifics = AndroidNotificationDetails(
//       '1', 'notification',
//       importance: Importance.max, priority: Priority.high);
//   var platformChannelSpecifics =
//   NotificationDetails(android: androidPlatformChannelSpecifics);
//   await flip.show(0, 'REMINDER', message, platformChannelSpecifics,
//       payload: 'Default_Sound');
// }
//
// class home_page extends StatefulWidget {
//   const home_page({super.key});
//
//   @override
//   State<home_page> createState() => _home_pageState();
// }
//
// class _home_pageState extends State<home_page> {
//   @override
//   void initState() {
//     super.initState();
//
//     Timer.periodic(Duration(seconds: 5), (timer) {
//       // getNotifications();
//       getdata();
//     });
//   }
//
//   Future<void> getdata() async {
//     SharedPreferences sh = await SharedPreferences.getInstance();
//     try {
//       String url = sh.getString('url').toString();
//       final urls = Uri.parse('$url/and_criminal_view_noti/');
//       String nid = "0";
//       if (sh.containsKey("nid")==false) {
//
//       } else {
//         nid = sh.getString('nid').toString();
//       }
//
//       var datas = await http.post(urls, body: {'nid': nid, });
//       var jsondata = json.decode(datas.body);
//       String status = jsondata['status'];
//       print(status);
//       if (status == "ok") {
//         String nid = jsondata['nid'].toString();
//         String message = jsondata['message'].toString();
//         // String billdate = jsondata['billdate'].toString();
//         sh.setString('nid',nid);
//         // if(nid != sh.getString('nid').toString()){
//         callbackDispatcher(message);
//         // }
//       }
//     } catch (e) {
//       print("Error: $e");
//     }
//   }
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       // drawer: const Drawer(
//       //   child: DrawerContent(),
//       // ),
//       appBar: AppBar(
//         backgroundColor: Colors.white,
//         elevation: 0,
//         iconTheme: const IconThemeData(color: Colors.black87),
//         // actions: const [
//         //   Icon(Icons.notifications_none),
//         //   SizedBox(width: 16),
//         // ],
//       ),
//       backgroundColor: const Color(0xFFF5F6FA),
//       body: Padding(
//         padding: const EdgeInsets.all(20.0),
//         child: Column(
//           crossAxisAlignment: CrossAxisAlignment.start,
//           children: [
//             const Row(
//               children: [
//                 CircleAvatar(
//                   backgroundImage: AssetImage('assets/user.jpg'),
//                   radius: 25,
//                 ),
//                 SizedBox(width: 12),
//                 Column(
//                   crossAxisAlignment: CrossAxisAlignment.start,
//                   children: [
//                     Text(
//                       'Hi Admin,',
//                       style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
//                     ),
//                     Text(
//                       'What do you want to do today?',
//                       style: TextStyle(color: Colors.black54),
//                     ),
//                   ],
//                 ),
//               ],
//             ),
//             const SizedBox(height: 30),
//             Container(
//               padding: const EdgeInsets.all(20),
//               decoration: BoxDecoration(
//                 color: Colors.white,
//                 borderRadius: BorderRadius.circular(20),
//               ),
//               child: Row(
//                 mainAxisAlignment: MainAxisAlignment.spaceBetween,
//                 children: const [
//                   Column(
//                     crossAxisAlignment: CrossAxisAlignment.start,
//                     children: [
//                       Text(''),
//                       SizedBox(height: 6),
//                       Text(
//                         '',
//                         style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
//                       ),
//                     ],
//                   ),
//                   Column(
//                     crossAxisAlignment: CrossAxisAlignment.start,
//                     children: [
//                       Text(''),
//                       SizedBox(height: 6),
//                       Text(
//                         '',
//                         style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
//                       ),
//                     ],
//                   ),
//                 ],
//               ),
//             ),
//             const SizedBox(height: 25),
//             const Text(
//               'Quick Actions',
//               style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
//             ),
//             const SizedBox(height: 15),
//             Expanded(
//               child: GridView.count(
//                 crossAxisCount: 2,
//                 crossAxisSpacing: 15,
//                 mainAxisSpacing: 15,
//                 children: [
//                   ActionCard(
//                     title: 'View Profile',
//                     color: Colors.pinkAccent,
//                     icon: Icons.verified_user,
//                     onTap: () {
//                       Navigator.push(
//                         context,
//                         MaterialPageRoute(builder: (context) => view_profilePage(title: '')),
//                       );
//                     },
//                   ),
//                   ActionCard(
//                     title: 'View Reply',
//                     color: Colors.deepPurple,
//                     icon: Icons.table_view_outlined,
//                     onTap: () {
//                       Navigator.push(
//                         context,
//                         MaterialPageRoute(builder: (context) => view_reply(title: '')),
//                       );
//                     },
//                   ),  ActionCard(
//                     title: 'Send Complaint',
//                     color: Colors.deepPurple,
//                     icon: Icons.table_view_outlined,
//                     onTap: () {
//                       Navigator.push(
//                         context,
//                         MaterialPageRoute(builder: (context) => send_complaint(title: '')),
//                       );
//                     },
//                   ), ActionCard(
//                     title: 'Change Password',
//                     color: Colors.deepPurple,
//                     icon: Icons.table_view_outlined,
//                     onTap: () {
//                       Navigator.push(
//                         context,
//                         MaterialPageRoute(builder: (context) => change_password(title: '')),
//                       );
//                     },
//                   ),ActionCard(
//               title: 'View Objects detected',
//               color: Colors.deepPurple,
//               icon: Icons.table_view_outlined,
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => viewobjdetection(title: '')),
//                 );
//               },
//                   ),ActionCard(
//               title: 'View Criminals detected',
//               color: Colors.deepPurple,
//               icon: Icons.table_view_outlined,
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => viewcrimdetection(title: '')),
//                 );
//               },
//                   ),
//
//                 ],
//               ),
//             ),
//
//           ],
//         ),
//       ),
//     );
//   }
// }
//
// class ActionCard extends StatelessWidget {
//   final String title;
//   final Color color;
//   final IconData icon;
//   final VoidCallback? onTap; // ADD this
//
//   const ActionCard({
//     super.key,
//     required this.title,
//     required this.color,
//     required this.icon,
//     this.onTap, // ADD this
//   });
//
//   @override
//   Widget build(BuildContext context) {
//     return GestureDetector(
//       onTap: onTap, // USE this
//       child: Container(
//         padding: const EdgeInsets.all(16),
//         decoration: BoxDecoration(
//           color: color.withOpacity(0.1),
//           borderRadius: BorderRadius.circular(20),
//         ),
//         child: Column(
//           crossAxisAlignment: CrossAxisAlignment.start,
//           children: [
//             CircleAvatar(
//               backgroundColor: color,
//               child: Icon(icon, color: Colors.white),
//             ),
//             const SizedBox(height: 10),
//             Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
//           ],
//         ),
//       ),
//     );
//   }
// }
import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;

import 'View_reply.dart';
import 'send_complaint.dart';
import 'view_criminaldetection.dart';
import 'view_objectdetection.dart';
import 'viewprofile.dart';
import 'Change_password.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: HomePage(),
  ));
}

// ────────────────────────────────────────────────
//  Notification Helper (kept similar but cleaner)
// ────────────────────────────────────────────────
Future<void> showNotification(String message) async {
  final flip = FlutterLocalNotificationsPlugin();

  const androidSettings = AndroidInitializationSettings('@mipmap/ic_launcher');
  const initSettings = InitializationSettings(android: androidSettings);

  await flip.initialize(initSettings);

  const androidDetails = AndroidNotificationDetails(
    'railway_reminder_channel',
    'Railway Reminders',
    importance: Importance.max,
    priority: Priority.high,
    showWhen: true,
  );

  const platformDetails = NotificationDetails(android: androidDetails);

  await flip.show(
    0,
    'New Update',
    message,
    platformDetails,
    payload: 'railway_notification',
  );
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  Timer? _timer;
  bool _isChecking = false;

  @override
  void initState() {
    super.initState();
    _startPolling();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _startPolling() {
    _timer = Timer.periodic(const Duration(seconds: 10), (_) {
      if (!_isChecking) _fetchNotifications();
    });
  }

  Future<void> _fetchNotifications() async {
    if (!mounted) return;
    setState(() => _isChecking = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? '';
      if (baseUrl.isEmpty) return;

      final uri = Uri.parse('$baseUrl/and_criminal_view_noti/');

      String lastNid = sh.getString('nid') ?? '0';

      final res = await http.post(uri, body: {'nid': lastNid});

      if (res.statusCode == 200 && mounted) {
        final data = json.decode(res.body);
        if (data['status'] == 'ok') {
          final newNid = data['nid']?.toString() ?? lastNid;
          final message = data['message']?.toString() ?? '';

          if (newNid != lastNid && message.isNotEmpty) {
            sh.setString('nid', newNid);
            await showNotification(message);
          }
        }
      }
    } catch (e) {
      // silent fail or log
      debugPrint("Notification poll error: $e");
    } finally {
      if (mounted) setState(() => _isChecking = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF0F4F8),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: const Text(
          "Admin Dashboard",
          style: TextStyle(
            color: Color(0xFF1A1F36),
            fontWeight: FontWeight.w700,
          ),
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 16),
            child: IconButton(
              icon: _isChecking
                  ? const SizedBox(
                width: 20,
                height: 20,
                child: CircularProgressIndicator(strokeWidth: 2.5),
              )
                  : const Icon(Icons.notifications_outlined),
              onPressed: _fetchNotifications,
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Greeting
              Row(
                children: [
                  CircleAvatar(
                    radius: 28,
                    backgroundColor: Colors.indigo.shade100,
                    child: const Icon(
                      Icons.admin_panel_settings_rounded,
                      size: 32,
                      color: Colors.indigo,
                    ),
                  ),
                  const SizedBox(width: 16),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        "Hello, Admin",
                        style: Theme.of(context).textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: const Color(0xFF1A1F36),
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        "Manage railway security today",
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          color: Colors.grey.shade700,
                        ),
                      ),
                    ],
                  ),
                ],
              ),

              const SizedBox(height: 32),

              // Quick Stats Cards (placeholders — connect real data later)
              Row(
                children: [
                  Expanded(
                    child: _StatCard(
                      title: "Objects Detected",
                      value: "142",
                      icon: Icons.camera_alt_outlined,
                      color: Colors.teal,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: _StatCard(
                      title: "Criminals Flagged",
                      value: "19",
                      icon: Icons.warning_amber_rounded,
                      color: Colors.redAccent,
                    ),
                  ),
                ],
              ),

              const SizedBox(height: 32),

              // Quick Actions Section
              Text(
                "Quick Actions",
                style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.w700,
                  color: const Color(0xFF1A1F36),
                ),
              ),

              const SizedBox(height: 16),

              GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: 2,
                crossAxisSpacing: 16,
                mainAxisSpacing: 16,
                childAspectRatio: 1.15,
                children: [
                  _ActionTile(
                    title: "View Profile",
                    icon: Icons.person_outline_rounded,
                    color: Colors.blue,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const ViewProfilePage()),
                    ),
                  ),
                  _ActionTile(
                    title: "View Replies",
                    icon: Icons.reply_all_rounded,
                    color: Colors.purple,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const ViewRepliesPage()),
                    ),
                  ),
                  _ActionTile(
                    title: "Send Complaint",
                    icon: Icons.report_problem_outlined,
                    color: Colors.orange,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const SendComplaintPage()),
                    ),
                  ),
                  _ActionTile(
                    title: "Change Password",
                    icon: Icons.lock_reset_rounded,
                    color: Colors.indigo,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const ChangePasswordPage()),
                    ),
                  ),
                  _ActionTile(
                    title: "Objects Detected",
                    icon: Icons.image_search_rounded,
                    color: Colors.teal,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const ViewObjectsDetectionPage()),
                    ),
                  ),
                  _ActionTile(
                    title: "Criminals Detected",
                    icon: Icons.security_rounded,
                    color: Colors.redAccent,
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const ViewCriminalsDetectionPage()),
                    ),
                  ),
                ],
              ),

              const SizedBox(height: 40),
            ],
          ),
        ),
      ),
    );
  }
}

// ────────────────────────────────────────────────
//  Reusable Stat Card
// ────────────────────────────────────────────────
class _StatCard extends StatelessWidget {
  final String title;
  final String value;
  final IconData icon;
  final Color color;

  const _StatCard({
    required this.title,
    required this.value,
    required this.icon,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.07),
            blurRadius: 12,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, color: color, size: 32),
          const SizedBox(height: 12),
          Text(
            value,
            style: const TextStyle(
              fontSize: 26,
              fontWeight: FontWeight.bold,
              color: Color(0xFF1A1F36),
            ),
          ),
          const SizedBox(height: 4),
          Text(
            title,
            style: TextStyle(
              fontSize: 14,
              color: Colors.grey.shade700,
            ),
          ),
        ],
      ),
    );
  }
}

// ────────────────────────────────────────────────
//  Modern Action Tile (glass-like)
// ────────────────────────────────────────────────
class _ActionTile extends StatelessWidget {
  final String title;
  final IconData icon;
  final Color color;
  final VoidCallback onTap;

  const _ActionTile({
    required this.title,
    required this.icon,
    required this.color,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.92),
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.06),
              blurRadius: 10,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: color.withOpacity(0.12),
                borderRadius: BorderRadius.circular(16),
              ),
              child: Icon(icon, color: color, size: 32),
            ),
            const SizedBox(height: 12),
            Text(
              title,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                height: 1.2,
              ),
            ),
          ],
        ),
      ),
    );
  }
}


// class DrawerContent extends StatefulWidget {
//   const DrawerContent({super.key});
//
//   @override
//   State<DrawerContent> createState() => _DrawerContentState();
// }

// class _DrawerContentState extends State<DrawerContent> {
//   void showDrawerMessage(String message) {
//     Navigator.pop(context); // Close drawer
//     ScaffoldMessenger.of(context).showSnackBar(
//       SnackBar(content: Text(message)),
//     );
//   }
//
//   // @override
//   // Widget build(BuildContext context) {
//   //   return ListView(
//   //     padding: EdgeInsets.zero,
//   //     children: [
//   //       const DrawerHeader(
//   //         decoration: BoxDecoration(color: Colors.blue),
//   //         child: Text('Menu', style: TextStyle(color: Colors.white, fontSize: 24)),
//   //       ),
//   //       ListTile(
//   //         leading: const Icon(Icons.dashboard),
//   //         title: const Text('Dashboard'),
//   //         onTap: () => showDrawerMessage('Dashboard selected'),
//   //       ),
//   //       ListTile(
//   //         leading: const Icon(Icons.receipt),
//   //         title: const Text('Add User'),
//   //         onTap: () => showDrawerMessage('Bills selected'),
//   //       ),
//   //       ListTile(
//   //         leading: const Icon(Icons.send),
//   //         title: const Text('Transfers'),
//   //         onTap: () => showDrawerMessage('Transfers selected'),
//   //       ),
//   //       ListTile(
//   //         leading: const Icon(Icons.settings),
//   //         title: const Text('Settings'),
//   //         onTap: () => showDrawerMessage('Settings selected'),
//   //       ),
//   //     ],
//   //   );
//   // }
// }
