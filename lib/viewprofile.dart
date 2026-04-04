// import 'package:flutter/material.dart';
// import 'package:http/http.dart' as http;
// import 'dart:convert';
// import 'package:fluttertoast/fluttertoast.dart';
//
// import 'package:shared_preferences/shared_preferences.dart';
//
// void main() {
//   runApp(const view_profile());
// }
//
// class view_profile extends StatelessWidget {
//   const view_profile({super.key});
//
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'View Profile',
//       theme: ThemeData(
//
//         colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
//         useMaterial3: true,
//       ),
//       home: const view_profilePage(title: 'View Profile'),
//     );
//   }
// }
//
// class view_profilePage extends StatefulWidget {
//   const view_profilePage({super.key, required this.title});
//
//   final String title;
//
//   @override
//   State<view_profilePage> createState() => _view_profilePageState();
// }
//
// class _view_profilePageState extends State<view_profilePage> {
//
//   _view_profilePageState()
//   {
//     _send_data();
//   }
//   @override
//   Widget build(BuildContext context) {
//
//
//
//     return WillPopScope(
//       onWillPop: () async{ return true; },
//       child: Scaffold(
//         appBar: AppBar(
//           leading: BackButton( ),
//           backgroundColor: Theme.of(context).colorScheme.primary,
//           title: Text(widget.title),
//         ),
//         body: SingleChildScrollView(
//           child: Column(
//             crossAxisAlignment: CrossAxisAlignment.start,
//             children: <Widget>[
//
//
//               // CircleAvatar(radius: 50,),
//               Column(
//                 children: [
//                   Image(image: NetworkImage(photo_),height: 200,width: 200,),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                   child: Text(name_),
//                   ),
//                   // Padding(
//                   //   padding: EdgeInsets.all(5),
//                   //   child: Text(dob_),
//                   // ),
//                   // Padding(
//                   //   padding: EdgeInsets.all(5),
//                   //   child: Text(gender_),
//                   // ),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                     child: Text(email_),
//                   ),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                     child: Text(phoneno_),
//                   ),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                     child: Text(place_),
//                   ),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                     child: Text(post_),
//                   ),
//                   Padding(
//                     padding: EdgeInsets.all(5),
//                     child: Text(pin_),
//                   ),
//                   // Padding(
//                   //   padding: EdgeInsets.all(5),
//                   //   child: Text(district_),
//                   // ),
//
//                 ],
//               ),
//               ElevatedButton(
//                 onPressed: () {
//                   // Navigator.push(context, MaterialPageRoute(
//                     // builder: (context) => MyEditPage(title: "Edit Profile"),));
//                 },
//                 child: Text("Edit Profile"),
//               ),
//
//             ],
//           ),
//         ),
//       ),
//     );
//   }
//
//
//   String name_="";
//   //String dob_="";
//   //String gender_="";
//   String email_="";
//   String phoneno_="";
//   String place_="";
//   String post_="";
//   String pin_="";
//   //String district_="";
//   String photo_="";
//
//   void _send_data() async{
//
//
//
//     SharedPreferences sh = await SharedPreferences.getInstance();
//     String url = sh.getString('url').toString();
//     String lid = sh.getString('lid').toString();
//     String img = sh.getString('img_url').toString();
//
//     final urls = Uri.parse('$url/app_view_profile/');
//     try {
//       final response = await http.post(urls, body: {
//       'lid':lid
//
//
//
//       });
//       if (response.statusCode == 200) {
//         String status = jsonDecode(response.body)['status'];
//         if (status=='ok') {
//           String name=jsonDecode(response.body)['name']         ;
//           // String dob=jsonDecode(response.body)['dob'];
//           // String gender=jsonDecode(response.body)['gender'];
//           String email=jsonDecode(response.body)['email'];
//           String phone=jsonDecode(response.body)['phoneno'];
//           String place=jsonDecode(response.body)['place'];
//           String post=jsonDecode(response.body)['post'];
//           String pin=jsonDecode(response.body)['pin'];
//           // String district=jsonDecode(response.body)['district'];
//           String photo=img+jsonDecode(response.body)['photo'];
//
//           setState(() {
//
//             name_= name;
//             // dob_= dob;
//             // gender_= gender;
//             email_= email;
//             phoneno_= phone;
//             place_= place;
//             post_= post;
//             pin_= pin;
//             // district_= district;
//             photo_= photo;
//           });
//
//
//
//
//
//         }else {
//           Fluttertoast.showToast(msg: 'Not Found');
//         }
//       }
//       else {
//         Fluttertoast.showToast(msg: 'Network Error');
//       }
//     }
//     catch (e){
//       Fluttertoast.showToast(msg: e.toString());
//     }
//   }
// }
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ViewProfilePage(),
  ));
}

class ViewProfilePage extends StatefulWidget {
  const ViewProfilePage({super.key});

  @override
  State<ViewProfilePage> createState() => _ViewProfilePageState();
}

class _ViewProfilePageState extends State<ViewProfilePage> {
  bool _isLoading = true;

  String name = '';
  String email = '';
  String phone = '';
  String place = '';
  String post = '';
  String pin = '';
  String photoUrl = '';

  @override
  void initState() {
    super.initState();
    _loadProfile();
  }

  Future<void> _loadProfile() async {
    final sh = await SharedPreferences.getInstance();
    final baseUrl = sh.getString('url') ?? '';
    final lid = sh.getString('lid') ?? '';
    final imgBase = sh.getString('img_url') ?? '';

    if (baseUrl.isEmpty || lid.isEmpty) {
      Fluttertoast.showToast(msg: "Missing configuration");
      setState(() => _isLoading = false);
      return;
    }

    try {
      final uri = Uri.parse('$baseUrl/app_view_profile/');
      final response = await http.post(uri, body: {'lid': lid});

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        if (data['status'] == 'ok') {
          setState(() {
            name = data['name'] ?? '';
            email = data['email'] ?? '';
            phone = data['phoneno'] ?? '';
            place = data['place'] ?? '';
            post = data['post'] ?? '';
            pin = data['pin'] ?? '';
            photoUrl = imgBase + (data['photo'] ?? '');

            _isLoading = false;
          });
        } else {
          Fluttertoast.showToast(msg: "Profile not found");
          setState(() => _isLoading = false);
        }
      } else {
        Fluttertoast.showToast(msg: "Network error");
        setState(() => _isLoading = false);
      }
    } catch (e) {
      Fluttertoast.showToast(msg: "Error: $e");
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF0F4F8),
      body: _isLoading
          ? const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircularProgressIndicator(),
            SizedBox(height: 16),
            Text("Loading profile..."),
          ],
        ),
      )
          : CustomScrollView(
        slivers: [
          // Modern gradient header with overlapping avatar
          SliverAppBar(
            expandedHeight: 220,
            pinned: true,
            backgroundColor: Colors.transparent,
            flexibleSpace: FlexibleSpaceBar(
              background: Container(
                decoration: const BoxDecoration(
                  gradient: LinearGradient(
                    colors: [Color(0xFF667EEA), Color(0xFF764BA2)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                ),
              ),
            ),
            leading: IconButton(
              icon: const Icon(Icons.arrow_back_ios_new, color: Colors.white),
              onPressed: () => Navigator.pop(context),
            ),
            title: const Text(
              "My Profile",
              style: TextStyle(color: Colors.white, fontWeight: FontWeight.w600),
            ),
            actions: [
              IconButton(
                icon: const Icon(Icons.edit, color: Colors.white),
                onPressed: () {
                  Fluttertoast.showToast(msg: "Edit Profile coming soon");
                  // Navigator.push(context, MaterialPageRoute(builder: (_) => EditProfilePage()));
                },
              ),
            ],
          ),

          SliverToBoxAdapter(
            child: Transform.translate(
              offset: const Offset(0, -60),
              child: Column(
                children: [
                  // Circular Profile Photo
                  Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      border: Border.all(color: Colors.white, width: 6),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.15),
                          blurRadius: 20,
                          offset: const Offset(0, 10),
                        ),
                      ],
                    ),
                    child: CircleAvatar(
                      radius: 68,
                      backgroundColor: Colors.white,
                      backgroundImage: photoUrl.isNotEmpty
                          ? NetworkImage(photoUrl)
                          : const AssetImage('assets/user.jpg') as ImageProvider,
                    ),
                  ),

                  const SizedBox(height: 16),

                  // Name
                  Text(
                    name.isNotEmpty ? name : "Admin User",
                    style: const TextStyle(
                      fontSize: 26,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF1A1F36),
                    ),
                  ),

                  const SizedBox(height: 32),

                  // Info Card
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 20),
                    child: Container(
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(24),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.08),
                            blurRadius: 15,
                            offset: const Offset(0, 6),
                          ),
                        ],
                      ),
                      child: Column(
                        children: [
                          _InfoTile(
                            icon: Icons.email_outlined,
                            title: "Email",
                            value: email,
                          ),
                          const Divider(height: 1, indent: 20, endIndent: 20),
                          _InfoTile(
                            icon: Icons.phone_outlined,
                            title: "Phone",
                            value: phone,
                          ),
                          const Divider(height: 1, indent: 20, endIndent: 20),
                          _InfoTile(
                            icon: Icons.location_on_outlined,
                            title: "Place",
                            value: place,
                          ),
                          const Divider(height: 1, indent: 20, endIndent: 20),
                          _InfoTile(
                            icon: Icons.location_city_outlined,
                            title: "Post",
                            value: post,
                          ),
                          const Divider(height: 1, indent: 20, endIndent: 20),
                          _InfoTile(
                            icon: Icons.pin_drop_outlined,
                            title: "Pin Code",
                            value: pin,
                          ),
                        ],
                      ),
                    ),
                  ),

                  const SizedBox(height: 40),

                  // Edit Button
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 20),
                    child: SizedBox(
                      width: double.infinity,
                      height: 56,
                      child: ElevatedButton(
                        onPressed: () {
                          Fluttertoast.showToast(msg: "Edit Profile coming soon");
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFFFF6B35),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(16),
                          ),
                          elevation: 3,
                        ),
                        child: const Text(
                          "Edit Profile",
                          style: TextStyle(
                            fontSize: 17,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                      ),
                    ),
                  ),

                  const SizedBox(height: 40),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

// Reusable Info Tile
class _InfoTile extends StatelessWidget {
  final IconData icon;
  final String title;
  final String value;

  const _InfoTile({
    required this.icon,
    required this.title,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: const Color(0xFF667EEA).withOpacity(0.1),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: const Color(0xFF667EEA), size: 24),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: TextStyle(
                    fontSize: 13,
                    color: Colors.grey.shade600,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                const SizedBox(height: 3),
                Text(
                  value.isNotEmpty ? value : "—",
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: Color(0xFF1A1F36),
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
