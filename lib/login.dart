// // import 'dart:convert';
//
// // import 'package:flutter/material.dart';
// // import 'package:fluttertoast/fluttertoast.dart';
// // import 'package:shared_preferences/shared_preferences.dart';
// // import 'package:http/http.dart' as http;
// //
// // import 'home.dart';
// //
// // void main() {
// //   runApp(const MyApp());
// // }
// //
// // class MyApp extends StatelessWidget {
// //   const MyApp({super.key});
// //
// //   @override
// //   Widget build(BuildContext context) {
// //     return MaterialApp(
// //       title: 'Flutter Demo',
// //       theme: ThemeData(
// //         colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
// //         useMaterial3: true,
// //       ),
// //       home: const MyLoginPage(title: 'Flutter Demo Home Page'),
// //     );
// //   }
// // }
// //
// // class MyLoginPage extends StatefulWidget {
// //   const MyLoginPage({super.key, required this.title});
// //
// //   final String title;
// //
// //   @override
// //   State<MyLoginPage> createState() => _MyLoginPageState();
// // }
// //
// // class _MyLoginPageState extends State<MyLoginPage> {
// //   // ✅ Create a TextEditingController
// //   final TextEditingController _usernametextController = TextEditingController();
// //   final TextEditingController _passwordtextController = TextEditingController();
// //
// //
// //
// //   @override
// //   Widget build(BuildContext context) {
// //     return Scaffold(
// //       appBar: AppBar(
// //         backgroundColor: Theme.of(context).colorScheme.inversePrimary,
// //         title: Text(widget.title),
// //       ),
// //       body: Center(
// //         child: Padding(
// //           padding: const EdgeInsets.all(16.0),
// //           child: Column(
// //             mainAxisAlignment: MainAxisAlignment.center,
// //             children: <Widget>[
// //               // ✅ TextField with controller
// //               TextField(
// //                 controller: _usernametextController,
// //                 decoration: const InputDecoration(
// //                   labelText: 'Enter Username or Email',
// //                   border: OutlineInputBorder(),
// //                 ),
// //               ),
// //               const SizedBox(height: 20),
// //               TextField(
// //                 controller: _passwordtextController,
// //                 decoration: const InputDecoration(
// //                   labelText: 'Enter Your Password',
// //                   border: OutlineInputBorder(),
// //                 ),
// //               ),
// //               const SizedBox(height: 20),
// //               // ✅ ElevatedButton
// //               ElevatedButton(
// //                 onPressed: () {
// //                 _send_data();
// //                 },
// //                 child: const Text('Login'),
// //               ),
// //             ],
// //           ),
// //         ),
// //       ),
// //     );
// //   }
// //   void _send_data() async{
// //
// //     String uname=_usernametextController.text;
// //     String password=_passwordtextController.text;
// //
// //     SharedPreferences sh = await SharedPreferences.getInstance();
// //     String url = sh.getString('url').toString();
// //
// //     final urls = Uri.parse('$url/flutter_logins/');
// //     try {
// //       final response = await http.post(urls, body: {
// //         'Username':uname,
// //         'Password':password,
// //       });
// //       if (response.statusCode == 200) {
// //         String status = jsonDecode(response.body)['status'];
// //         if (status=='ok') {
// //           String lid=jsonDecode(response.body)['lid'];
// //           sh.setString("lid", lid);
// //
// //           Navigator.push(context, MaterialPageRoute(
// //             builder: (context) => HomePage(),));
// //         }else {
// //           Fluttertoast.showToast(msg: 'Not Found');
// //         }
// //       }
// //       else {
// //         Fluttertoast.showToast(msg: 'Network Error');
// //       }
// //     }
// //     catch (e){
// //       Fluttertoast.showToast(msg: e.toString());
// //     }
// //   }
// //
// // }
// import 'dart:convert';
// import 'package:flutter/material.dart';
// import 'package:fluttertoast/fluttertoast.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
//
// import 'main.dart';
// import 'newhome.dart';
//
// void main() {
//   runApp(const MaterialApp(
//     debugShowCheckedModeBanner: false,
//     home: MyLoginPage(title: 'Login'),
//   ));
// }
//
// class MyLoginPage extends StatefulWidget {
//   const MyLoginPage({super.key, required this.title});
//   final String title;
//
//   @override
//   State<MyLoginPage> createState() => _MyLoginPageState();
// }
//
// class _MyLoginPageState extends State<MyLoginPage> {
//   final TextEditingController _usernametextController = TextEditingController();
//   final TextEditingController _passwordtextController = TextEditingController();
//
//   @override
//   Widget build(BuildContext context) {
//     return WillPopScope(
//         onWillPop: () async {
//       Navigator.pushReplacement(
//         context,
//         MaterialPageRoute(builder: (context) => const MyHomePage(title: '',)),
//       );
//       return false; // Prevent default pop
//     },
//     child:Scaffold(
//       backgroundColor: const Color(0xFFEFF3FF), // Light blue background
//       body: SingleChildScrollView(
//         child: Column(
//           children: [
//             // Top Shape and Logo
//             Stack(
//               children: [
//                 Container(
//                   height: 180,
//                   decoration: const BoxDecoration(
//                     color: Color(0xFF0047AB),
//                     borderRadius:
//                     BorderRadius.only(bottomLeft: Radius.circular(80)),
//                   ),
//                 ),
//                 const Positioned(
//                   top: 100,
//                   left: 20,
//                   child: Text(
//                     'Login Page',
//                     style: TextStyle(
//                         fontSize: 32,
//                         color: Colors.white,
//                         fontWeight: FontWeight.bold),
//                   ),
//                 ),
//               ],
//             ),
//
//             const SizedBox(height: 40),
//
//             Padding(
//               padding: const EdgeInsets.symmetric(horizontal: 24.0),
//               child: Column(
//                 crossAxisAlignment: CrossAxisAlignment.start,
//                 children: [
//                   const Text("Email id",
//                       style:
//                       TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
//                   const SizedBox(height: 10),
//                   TextField(
//                     controller: _usernametextController,
//                     decoration: InputDecoration(
//                       hintText: "Enter your email",
//                       filled: true,
//                       fillColor: Colors.white,
//                       border: OutlineInputBorder(
//                           borderRadius: BorderRadius.circular(8),
//                           borderSide: BorderSide.none),
//                     ),
//                   ),
//                   const SizedBox(height: 20),
//                   const Text("Password",
//                       style:
//                       TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
//                   const SizedBox(height: 10),
//                   TextField(
//                     controller: _passwordtextController,
//                     obscureText: true,
//                     decoration: InputDecoration(
//                       hintText: "••••••••",
//                       filled: true,
//                       fillColor: Colors.white,
//                       border: OutlineInputBorder(
//                           borderRadius: BorderRadius.circular(8),
//                           borderSide: BorderSide.none),
//                     ),
//                   ),
//                   const SizedBox(height: 30),
//
//                   // Login Button
//                   SizedBox(
//                     width: double.infinity,
//                     child: ElevatedButton(
//                       onPressed: _send_data,
//                       style: ElevatedButton.styleFrom(
//                         padding: const EdgeInsets.symmetric(vertical: 16),
//                         backgroundColor: Colors.orange,
//                         shape: RoundedRectangleBorder(
//                             borderRadius: BorderRadius.circular(12)),
//                       ),
//                       child: const Text("Login",
//                           style: TextStyle(color: Colors.white, fontSize: 16)),
//                     ),
//                   ),
//
//                   const SizedBox(height: 10),
//                   Align(
//                     alignment: Alignment.centerRight,
//                     child: TextButton(
//                       onPressed: () {},
//                       child: const Text("Forgot Password ?",
//                           style: TextStyle(color: Colors.black87)),
//                     ),
//                   ),
//                   const SizedBox(height: 10),
//
//                   // Divider
//                   Row(children: const <Widget>[
//                     Expanded(child: Divider()),
//                     Padding(
//                       padding: EdgeInsets.symmetric(horizontal: 8),
//                       child: Text("or"),
//                     ),
//                     Expanded(child: Divider()),
//                   ]),
//                   const SizedBox(height: 20),
//
//                   // Facebook Button
//                   // SizedBox(
//                   //   width: double.infinity,
//                   //   child: ElevatedButton.icon(
//                   //     onPressed: () {},
//                   //     icon: const Icon(Icons.facebook, color: Colors.white),
//                   //     label: const Text("Log in with Facebook"),
//                   //     style: ElevatedButton.styleFrom(
//                   //         backgroundColor: const Color(0xFF1877F2),
//                   //         padding: const EdgeInsets.symmetric(vertical: 14),
//                   //         shape: RoundedRectangleBorder(
//                   //             borderRadius: BorderRadius.circular(8))),
//                   //   ),
//                   // ),
//                   const SizedBox(height: 30),
//
//                   // Register Prompt
//                   Row(
//                     mainAxisAlignment: MainAxisAlignment.center,
//                     children: const [
//                       Text("Don't have an account? ",
//                           style: TextStyle(color: Colors.black87)),
//                       Text("Register",
//                           style: TextStyle(
//                               fontWeight: FontWeight.bold,
//                               color: Colors.orange)),
//                     ],
//                   ),
//                 ],
//               ),
//             )
//           ],
//         ),
//       ),
//     ));
//   }
//
//   void _send_data() async {
//     String uname = _usernametextController.text;
//     String password = _passwordtextController.text;
//
//     SharedPreferences sh = await SharedPreferences.getInstance();
//     String url = sh.getString('url').toString();
//
//     final urls = Uri.parse('$url/app_login_post/');
//     try {
//       final response = await http.post(urls, body: {
//         'username': uname,
//         'password': password,
//       });
//       if (response.statusCode == 200) {
//         String status = jsonDecode(response.body)['status'];
//         if (status == 'ok') {
//           String lid = jsonDecode(response.body)['lid'];
//           sh.setString("lid", lid);
//
//           Navigator.push(
//             context,
//             MaterialPageRoute(builder: (context) => home_page()),
//           );
//         } else {
//           Fluttertoast.showToast(msg: 'Not Found');
//         }
//       } else {
//         Fluttertoast.showToast(msg: 'Network Error');
//       }
//     } catch (e) {
//       Fluttertoast.showToast(msg: e.toString());
//     }
//   }
// }
//


import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;

import 'newhome.dart'; // ← your home page

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: LoginPage(),
  ));
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();
  final _passwordController = TextEditingController();

  bool _obscurePassword = true;
  bool _isLoading = false;

  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _login() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? 'http://your-default-url.com';
      final uri = Uri.parse('$baseUrl/app_login_post/');

      final response = await http.post(
        uri,
        body: {
          'username': _usernameController.text.trim(),
          'password': _passwordController.text,
        },
      );

      if (!mounted) return;

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final status = data['status'] as String?;

        if (status == 'ok') {
          final lid = data['lid']?.toString();
          if (lid != null) {
            await sh.setString('lid', lid);
            if (mounted) {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(builder: (_) => const HomePage()),
              );
            }
          } else {
            Fluttertoast.showToast(msg: 'Invalid response');
          }
        } else {
          Fluttertoast.showToast(msg: 'Invalid credentials');
        }
      } else {
        Fluttertoast.showToast(msg: 'Server error • ${response.statusCode}');
      }
    } catch (e) {
      Fluttertoast.showToast(msg: 'Error: $e');
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color(0xFF667EEA), Color(0xFF764BA2)],
          ),
        ),
        child: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 24),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    // Logo / App Name Area
                    const Icon(
                      Icons.lock_outline_rounded,
                      size: 80,
                      color: Colors.white,
                    ),
                    const SizedBox(height: 16),
                    const Text(
                      "Welcome Back",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 32,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                        letterSpacing: 0.5,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      "Sign in to continue",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 16,
                        color: Colors.white.withOpacity(0.85),
                      ),
                    ),

                    const SizedBox(height: 48),

                    // Card-like container with subtle elevation / glass effect
                    Container(
                      padding: const EdgeInsets.all(24),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.95),
                        borderRadius: BorderRadius.circular(28),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.15),
                            blurRadius: 20,
                            offset: const Offset(0, 10),
                          ),
                        ],
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          // Email / Username
                          const Text(
                            "Email / Username",
                            style: TextStyle(
                              fontWeight: FontWeight.w600,
                              fontSize: 15,
                              color: Color(0xFF2D3748),
                            ),
                          ),
                          const SizedBox(height: 8),
                          TextFormField(
                            controller: _usernameController,
                            keyboardType: TextInputType.emailAddress,
                            textInputAction: TextInputAction.next,
                            decoration: InputDecoration(
                              hintText: "example@email.com",
                              prefixIcon: const Icon(Icons.person_outline_rounded),
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(16),
                                borderSide: BorderSide.none,
                              ),
                              filled: true,
                              fillColor: const Color(0xFFF7FAFC),
                              contentPadding: const EdgeInsets.symmetric(
                                vertical: 16,
                                horizontal: 16,
                              ),
                            ),
                            validator: (value) {
                              if (value == null || value.trim().isEmpty) {
                                return 'Please enter your email/username';
                              }
                              return null;
                            },
                          ),

                          const SizedBox(height: 24),

                          // Password
                          const Text(
                            "Password",
                            style: TextStyle(
                              fontWeight: FontWeight.w600,
                              fontSize: 15,
                              color: Color(0xFF2D3748),
                            ),
                          ),
                          const SizedBox(height: 8),
                          TextFormField(
                            controller: _passwordController,
                            obscureText: _obscurePassword,
                            textInputAction: TextInputAction.done,
                            decoration: InputDecoration(
                              hintText: "••••••••",
                              prefixIcon: const Icon(Icons.lock_outline_rounded),
                              suffixIcon: IconButton(
                                icon: Icon(
                                  _obscurePassword
                                      ? Icons.visibility_off_outlined
                                      : Icons.visibility_outlined,
                                ),
                                onPressed: () {
                                  setState(() => _obscurePassword = !_obscurePassword);
                                },
                              ),
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(16),
                                borderSide: BorderSide.none,
                              ),
                              filled: true,
                              fillColor: const Color(0xFFF7FAFC),
                              contentPadding: const EdgeInsets.symmetric(
                                vertical: 16,
                                horizontal: 16,
                              ),
                            ),
                            validator: (value) {
                              if (value == null || value.isEmpty) {
                                return 'Please enter your password';
                              }
                              if (value.length < 6) {
                                return 'Password must be at least 6 characters';
                              }
                              return null;
                            },
                          ),

                          const SizedBox(height: 12),
                          Align(
                            alignment: Alignment.centerRight,
                            child: TextButton(
                              onPressed: () {
                                // TODO: Forgot password screen
                                Fluttertoast.showToast(msg: "Forgot password clicked");
                              },
                              child: const Text(
                                "Forgot Password?",
                                style: TextStyle(
                                  color: Color(0xFF667EEA),
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ),
                          ),

                          const SizedBox(height: 16),

                          // Login Button
                          SizedBox(
                            height: 56,
                            child: ElevatedButton(
                              onPressed: _isLoading ? null : _login,
                              style: ElevatedButton.styleFrom(
                                backgroundColor: const Color(0xFFFF6B35),
                                foregroundColor: Colors.white,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(16),
                                ),
                                elevation: 2,
                              ),
                              child: _isLoading
                                  ? const SizedBox(
                                height: 24,
                                width: 24,
                                child: CircularProgressIndicator(
                                  color: Colors.white,
                                  strokeWidth: 2.5,
                                ),
                              )
                                  : const Text(
                                "Sign In",
                                style: TextStyle(
                                  fontSize: 17,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 32),

                    // Register row
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          "Don't have an account? ",
                          style: TextStyle(color: Colors.white.withOpacity(0.9)),
                        ),
                        GestureDetector(
                          onTap: () {
                            // TODO: Navigate to Register
                            Fluttertoast.showToast(msg: "Go to Register screen");
                          },
                          child: const Text(
                            "Register",
                            style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}