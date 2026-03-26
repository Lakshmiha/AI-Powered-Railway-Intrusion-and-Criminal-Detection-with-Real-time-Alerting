// import 'dart:convert';
// import 'dart:io';
// import 'package:flutter/material.dart';
// import 'package:fluttertoast/fluttertoast.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
// import 'package:image_picker/image_picker.dart';
// import 'login.dart';
// import 'newhome.dart';
//
//
// void main() {
//   runApp( change_password(title: '',));
// }
//
// class change_password extends StatefulWidget {
//   const change_password({super.key, required this.title});
//
//   final String title;
//   @override
//   State<change_password> createState() => _change_passwordState();
//
// }
// class _change_passwordState extends State<change_password> {
//
//   final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
//   final TextEditingController _oldpasstextController = TextEditingController();
//   final TextEditingController _newpasstextController = TextEditingController();
//   final TextEditingController _confirmpasstextController = TextEditingController();
//
//   File? _selectedImage;
//   Future<void> _chooseImage() async {
//     final pickedFile = await ImagePicker().pickImage(source: ImageSource.gallery);
//     if (pickedFile != null) {
//       setState(() {
//         _selectedImage = File(pickedFile.path);
//       });
//     }
//     else {
//       Fluttertoast.showToast(msg: "No image selected");
//     }
//   }
//
//   Future<void> _sendData() async {
//     String currentpassword = _oldpasstextController.text;
//     String newpassword = _newpasstextController.text;
//     String confirmpassword = _confirmpasstextController.text;
//
//     SharedPreferences sh = await SharedPreferences.getInstance();
//     String? url = sh.getString('url');
//     String? lid = sh.getString('lid');
//
//     if (url == null) {
//       Fluttertoast.showToast(msg: "Server URL not found.");
//       return;
//     }
//
//     final uri = Uri.parse('$url/app_change_password_post/');
//     var request = http.MultipartRequest('POST', uri);
//     request.fields['currentpassword'] = currentpassword;
//     request.fields['newpassword'] = newpassword;
//     request.fields['confirmpassword'] = confirmpassword;
//     request.fields['lid'] = lid!;
//
//     // if (_selectedImage != null) {
//     //   request.files.add(await http.MultipartFile.fromPath('photo', _selectedImage!.path));
//     // }
//
//     try {
//       var response = await request.send();
//       var respStr = await response.stream.bytesToString();
//       var data = jsonDecode(respStr);
//
//       if (response.statusCode == 200 && data['status'] == 'ok') {
//         Fluttertoast.showToast(msg: "Submitted successfully.");
//
//         Navigator.push(context, MaterialPageRoute(builder: (context)=>LoginPage()));
//       } else {
//         Fluttertoast.showToast(msg: "Submission failed.");
//       }
//     } catch (e) {
//       Fluttertoast.showToast(msg: "Error: $e");
//     }
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return WillPopScope(
//       onWillPop: () async {
//         Navigator.pushReplacement(
//           context,
//           MaterialPageRoute(builder: (context) => const HomePage()),
//         );
//         return false;
//       },
//       child: Scaffold(
//         appBar: AppBar(
//           title: Text(widget.title),
//           centerTitle: true,
//           backgroundColor: Theme.of(context).colorScheme.primary,
//           foregroundColor: Colors.white,
//         ),
//         body: SingleChildScrollView(
//           padding: const EdgeInsets.all(16),
//           child: Form(
//             key: _formKey,
//             child: Column(
//               children: [
//
//                 TextFormField(
//                   controller: _oldpasstextController,
//                   decoration: const InputDecoration(
//                     labelText: 'Enter Your Old Password',
//                     border: OutlineInputBorder(),
//                   ),
//                   validator: (value) {
//                     if (value == null || value.trim().isEmpty) {
//                       return 'Old password is required';
//                     }
//                     return null;
//                   },
//                 ),
//                 const SizedBox(height: 10),
//                 TextFormField(
//                   controller: _newpasstextController,
//                   decoration: const InputDecoration(
//                     labelText: 'Enter Your New Password',
//                     border: OutlineInputBorder(),
//                   ),
//                   validator: (value) {
//                     if (value == null || value.trim().isEmpty) {
//                       return 'New password is required';
//                     }
//                     if (!RegExp(
//                         r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$')
//                         .hasMatch(value)) {
//                       return 'Password must be 8+ chars, include uppercase, lowercase, number & special character';
//                     }
//                     return null;
//                   },
//                 ),
//                 const SizedBox(height: 10),
//                 TextFormField(
//                   controller: _confirmpasstextController,
//                   decoration: const InputDecoration(
//                     labelText: 'Confirm password',
//                     border: OutlineInputBorder(),
//                   ),
//                   validator: (value) {
//                     if (value == null || value.trim().isEmpty) {
//                       return 'Confirm password is required';
//                     }
//                     if (value!=_newpasstextController.text) {
//                       return "Password doesn't match!!";
//                     }
//                     return null;
//                   },
//                 ),
//                 const SizedBox(height: 20),
//                 ElevatedButton(
//                   onPressed: () {
//                     if (_formKey.currentState!.validate()) {
//                       _sendData();
//                     } else {
//                       Fluttertoast.showToast(msg: "Please fix errors in the form");
//                     }
//                   },
//                   child: const Text("Submit"),
//                   style: ElevatedButton.styleFrom(
//                     minimumSize: const Size.fromHeight(50),
//                   ),
//                 ),
//               ],
//             ),
//           ),
//         ),
//       ),
//     );
//   }
// }
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'login.dart';
import 'newhome.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ChangePasswordPage(),
  ));
}

class ChangePasswordPage extends StatefulWidget {
  const ChangePasswordPage({super.key});

  @override
  State<ChangePasswordPage> createState() => _ChangePasswordPageState();
}

class _ChangePasswordPageState extends State<ChangePasswordPage> {
  final _formKey = GlobalKey<FormState>();

  final _oldPasswordCtrl = TextEditingController();
  final _newPasswordCtrl = TextEditingController();
  final _confirmPasswordCtrl = TextEditingController();

  bool _obscureOld = true;
  bool _obscureNew = true;
  bool _obscureConfirm = true;
  bool _isLoading = false;

  String _passwordStrength = '';
  Color _strengthColor = Colors.grey;

  @override
  void initState() {
    super.initState();
    _newPasswordCtrl.addListener(_updatePasswordStrength);
  }

  @override
  void dispose() {
    _oldPasswordCtrl.dispose();
    _newPasswordCtrl.dispose();
    _confirmPasswordCtrl.dispose();
    super.dispose();
  }

  void _updatePasswordStrength() {
    final pass = _newPasswordCtrl.text;
    if (pass.isEmpty) {
      setState(() {
        _passwordStrength = '';
        _strengthColor = Colors.grey;
      });
      return;
    }

    bool hasUpper = pass.contains(RegExp(r'[A-Z]'));
    bool hasLower = pass.contains(RegExp(r'[a-z]'));
    bool hasDigit = pass.contains(RegExp(r'\d'));
    bool hasSpecial = pass.contains(RegExp(r'[@$!%*?&]'));
    int length = pass.length;

    int score = 0;
    if (length >= 8) score++;
    if (hasUpper) score++;
    if (hasLower) score++;
    if (hasDigit) score++;
    if (hasSpecial) score++;

    setState(() {
      if (score <= 2) {
        _passwordStrength = 'Weak';
        _strengthColor = Colors.red;
      } else if (score == 3) {
        _passwordStrength = 'Fair';
        _strengthColor = Colors.orange;
      } else if (score == 4) {
        _passwordStrength = 'Good';
        _strengthColor = Colors.blue;
      } else {
        _passwordStrength = 'Strong';
        _strengthColor = Colors.green.shade700;
      }
    });
  }

  Future<void> _changePassword() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? '';
      final lid = sh.getString('lid') ?? '';

      if (baseUrl.isEmpty || lid.isEmpty) {
        Fluttertoast.showToast(msg: "Missing configuration");
        return;
      }

      final uri = Uri.parse('$baseUrl/app_change_password_post/');

      final response = await http.post(uri, body: {
        'currentpassword': _oldPasswordCtrl.text,
        'newpassword': _newPasswordCtrl.text,
        'confirmpassword': _confirmPasswordCtrl.text,
        'lid': lid,
      });

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['status'] == 'ok') {
          Fluttertoast.showToast(
            msg: "Password changed successfully. Please login again.",
            backgroundColor: Colors.green.shade700,
          );

          // Clear login data
          await sh.remove('lid');
          // Optionally clear more keys if needed

          if (mounted) {
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (_) => const LoginPage()),
            );
          }
          return;
        } else {
          final msg = data['message'] ?? "Change failed";
          Fluttertoast.showToast(msg: msg);
        }
      } else {
        Fluttertoast.showToast(msg: "Server error • ${response.statusCode}");
      }
    } catch (e) {
      Fluttertoast.showToast(msg: "Error: $e");
    } finally {
      if (mounted) setState(() => _isLoading = false);
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
        backgroundColor: const Color(0xFFF8FAFC),
        appBar: AppBar(
          elevation: 0,
          backgroundColor: Colors.transparent,
          foregroundColor: Colors.black87,
          title: const Text(
            "Change Password",
            style: TextStyle(fontWeight: FontWeight.w700),
          ),
          centerTitle: true,
        ),
        body: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
            child: Form(
              key: _formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Hint card
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.amber.shade50,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: Colors.amber.shade200),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(Icons.shield_outlined, color: Colors.amber.shade800),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            "Choose a strong password that you haven't used before.",
                            style: TextStyle(color: Colors.amber.shade900),
                          ),
                        ),
                      ],
                    ),
                  ),

                  const SizedBox(height: 32),

                  // Old Password
                  TextFormField(
                    controller: _oldPasswordCtrl,
                    obscureText: _obscureOld,
                    textInputAction: TextInputAction.next,
                    decoration: InputDecoration(
                      labelText: "Current Password",
                      prefixIcon: const Icon(Icons.lock_outline_rounded),
                      suffixIcon: IconButton(
                        icon: Icon(_obscureOld ? Icons.visibility_off : Icons.visibility),
                        onPressed: () => setState(() => _obscureOld = !_obscureOld),
                      ),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                      filled: true,
                      fillColor: Colors.white,
                    ),
                    validator: (v) => (v?.trim().isEmpty ?? true) ? "Required" : null,
                  ),

                  const SizedBox(height: 24),

                  // New Password
                  TextFormField(
                    controller: _newPasswordCtrl,
                    obscureText: _obscureNew,
                    textInputAction: TextInputAction.next,
                    decoration: InputDecoration(
                      labelText: "New Password",
                      prefixIcon: const Icon(Icons.lock_reset_rounded),
                      suffixIcon: IconButton(
                        icon: Icon(_obscureNew ? Icons.visibility_off : Icons.visibility),
                        onPressed: () => setState(() => _obscureNew = !_obscureNew),
                      ),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                      filled: true,
                      fillColor: Colors.white,
                      helperText: _passwordStrength.isNotEmpty ? "Strength: $_passwordStrength" : null,
                      helperStyle: TextStyle(color: _strengthColor),
                    ),
                    validator: (v) {
                      if (v == null || v.trim().isEmpty) return "Required";
                      if (!RegExp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$').hasMatch(v)) {
                        return "Must be 8+ chars with upper, lower, number & symbol";
                      }
                      return null;
                    },
                  ),

                  const SizedBox(height: 24),

                  // Confirm Password
                  TextFormField(
                    controller: _confirmPasswordCtrl,
                    obscureText: _obscureConfirm,
                    textInputAction: TextInputAction.done,
                    decoration: InputDecoration(
                      labelText: "Confirm New Password",
                      prefixIcon: const Icon(Icons.lock_outline_rounded),
                      suffixIcon: IconButton(
                        icon: Icon(_obscureConfirm ? Icons.visibility_off : Icons.visibility),
                        onPressed: () => setState(() => _obscureConfirm = !_obscureConfirm),
                      ),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
                      filled: true,
                      fillColor: Colors.white,
                    ),
                    validator: (v) {
                      if (v == null || v.trim().isEmpty) return "Required";
                      if (v != _newPasswordCtrl.text) return "Passwords do not match";
                      return null;
                    },
                  ),

                  const SizedBox(height: 40),

                  // Submit Button
                  SizedBox(
                    height: 56,
                    child: ElevatedButton.icon(
                      onPressed: _isLoading ? null : () {
                        if (_formKey.currentState!.validate()) {
                          _changePassword();
                        }
                      },
                      icon: _isLoading
                          ? const SizedBox.shrink()
                          : const Icon(Icons.check_circle_outline_rounded),
                      label: _isLoading
                          ? const SizedBox(
                        height: 20,
                        width: 20,
                        child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2.5),
                      )
                          : const Text(
                        "Update Password",
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
                      ),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.indigo.shade700,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                        elevation: 2,
                      ),
                    ),
                  ),

                  const SizedBox(height: 24),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}