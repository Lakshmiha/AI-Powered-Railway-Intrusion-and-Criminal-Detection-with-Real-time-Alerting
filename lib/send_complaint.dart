// import 'dart:convert';
// import 'dart:io';
// import 'package:flutter/material.dart';
// import 'package:fluttertoast/fluttertoast.dart';
// import 'package:shared_preferences/shared_preferences.dart';
// import 'package:http/http.dart' as http;
// import 'package:image_picker/image_picker.dart';
// import 'View_reply.dart';
// import 'newhome.dart';
//
//
// void main() {
//   runApp( send_complaint(title: '',));
// }
//
// class send_complaint extends StatefulWidget {
//   const send_complaint({super.key, required this.title});
//
//   final String title;
//   @override
//   State<send_complaint> createState() => _send_complaintState();
//
// }
// class _send_complaintState extends State<send_complaint> {
//
//   final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
//   final TextEditingController _sendcomplaintController = TextEditingController();
//   // final TextEditingController _emailtextController = TextEditingController();
//   // final TextEditingController _phonenotextController = TextEditingController();
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
//     String complaint = _sendcomplaintController.text;
//     // String uemail = _emailtextController.text;
//     // String uphone = _phonenotextController.text;
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
//     final uri = Uri.parse('$url/app_sendcomplaint_post/');
//     var request = http.MultipartRequest('POST', uri);
//     request.fields['complaint'] = complaint;
//     request.fields['lid'] = lid!;
//     // request.fields['uphoneno'] = uphone;
//
//
//
//     try {
//       var response = await request.send();
//       var respStr = await response.stream.bytesToString();
//       var data = jsonDecode(respStr);
//
//       if (response.statusCode == 200 && data['status'] == 'ok') {
//         Fluttertoast.showToast(msg: "Submitted successfully.");
//         Navigator.push(
//           context,
//           MaterialPageRoute(builder: (context) => const ViewRepliesPage()),
//         );
//
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
//                 const SizedBox(height: 20),
//                 TextFormField(
//                   controller: _sendcomplaintController,
//                   decoration: const InputDecoration(
//                     labelText: 'Enter Your Name',
//                     border: OutlineInputBorder(),
//                   ),
//                   validator: (value) {
//                     if (value == null || value.trim().isEmpty) {
//                       return 'Enter the complaint';
//                     }
//                     return null;
//                   },
//                 ),
//
//                 const SizedBox(height: 20),
//                 ElevatedButton(
//                   onPressed: () {
//                     if (_formKey.currentState!.validate()) {
//                       _sendData();
//                     } else {
//                       Fluttertoast.showToast(msg: "Please fix errors in the form");
//                     }
//                   },
//                   child: const Text("Send"),
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
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'View_reply.dart';
import 'newhome.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: SendComplaintPage(),
  ));
}

class SendComplaintPage extends StatefulWidget {
  const SendComplaintPage({super.key});

  @override
  State<SendComplaintPage> createState() => _SendComplaintPageState();
}

class _SendComplaintPageState extends State<SendComplaintPage> {
  final _formKey = GlobalKey<FormState>();
  final _complaintController = TextEditingController();
  File? _selectedImage;
  bool _isLoading = false;
  int _charCount = 0;

  final int _maxChars = 500;

  @override
  void initState() {
    super.initState();
    _complaintController.addListener(() {
      setState(() => _charCount = _complaintController.text.length);
    });
  }

  @override
  void dispose() {
    _complaintController.dispose();
    super.dispose();
  }

  Future<void> _pickImage() async {
    try {
      final picker = ImagePicker();
      final picked = await picker.pickImage(source: ImageSource.gallery);
      if (picked != null && mounted) {
        setState(() => _selectedImage = File(picked.path));
      }
    } catch (e) {
      Fluttertoast.showToast(msg: "Failed to pick image");
    }
  }

  Future<void> _removeImage() async {
    setState(() => _selectedImage = null);
  }

  Future<void> _submitComplaint() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      final sh = await SharedPreferences.getInstance();
      final baseUrl = sh.getString('url') ?? '';
      final lid = sh.getString('lid') ?? '';

      if (baseUrl.isEmpty || lid.isEmpty) {
        Fluttertoast.showToast(msg: "Configuration missing");
        return;
      }

      final uri = Uri.parse('$baseUrl/app_sendcomplaint_post/');
      var request = http.MultipartRequest('POST', uri);

      request.fields['complaint'] = _complaintController.text.trim();
      request.fields['lid'] = lid;

      if (_selectedImage != null) {
        request.files.add(await http.MultipartFile.fromPath(
          'photo', // ← adjust field name if your backend expects different key
          _selectedImage!.path,
        ));
      }

      final streamed = await request.send();
      final response = await http.Response.fromStream(streamed);

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['status'] == 'ok') {
          Fluttertoast.showToast(
            msg: "Complaint submitted successfully",
            backgroundColor: Colors.green.shade700,
          );

          if (mounted) {
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (_) => const ViewRepliesPage()),
            );
          }
          return;
        }
      }

      Fluttertoast.showToast(msg: "Submission failed. Try again.");
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
        backgroundColor: const Color(0xFFF5F7FA),
        appBar: AppBar(
          elevation: 0,
          backgroundColor: Colors.transparent,
          foregroundColor: Colors.black87,
          title: const Text(
            "New Complaint",
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
                  // Header hint
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.blue.shade50,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.info_outline_rounded, color: Colors.blue.shade700),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            "Please describe the issue clearly. Attach photo if available.",
                            style: TextStyle(color: Colors.blue.shade800),
                          ),
                        ),
                      ],
                    ),
                  ),

                  const SizedBox(height: 32),

                  // Complaint field
                  TextFormField(
                    controller: _complaintController,
                    maxLines: 6,
                    maxLength: _maxChars,
                    textCapitalization: TextCapitalization.sentences,
                    decoration: InputDecoration(
                      labelText: "Describe your complaint",
                      hintText: "What happened? Where? When? Any details...",
                      alignLabelWithHint: true,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(16),
                        borderSide: BorderSide.none,
                      ),
                      filled: true,
                      fillColor: Colors.white,
                      counterStyle: TextStyle(
                        color: _charCount > _maxChars * 0.9 ? Colors.red : Colors.grey,
                      ),
                      contentPadding: const EdgeInsets.symmetric(
                        horizontal: 20,
                        vertical: 16,
                      ),
                    ),
                    validator: (value) {
                      if (value == null || value.trim().isEmpty) {
                        return 'Please enter your complaint';
                      }
                      if (value.trim().length < 10) {
                        return 'Complaint is too short';
                      }
                      return null;
                    },
                  ),

                  const SizedBox(height: 32),

                  // Image picker + preview
                  GestureDetector(
                    onTap: _isLoading ? null : _pickImage,
                    child: Container(
                      height: 160,
                      decoration: BoxDecoration(
                        color: Colors.grey.shade100,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(
                          color: Colors.grey.shade300,
                          width: 1.5,
                          style: _selectedImage == null ? BorderStyle.solid : BorderStyle.none,
                        ),
                      ),
                      child: _selectedImage != null
                          ? Stack(
                        fit: StackFit.expand,
                        children: [
                          ClipRRect(
                            borderRadius: BorderRadius.circular(16),
                            child: Image.file(
                              _selectedImage!,
                              fit: BoxFit.cover,
                            ),
                          ),
                          Positioned(
                            top: 8,
                            right: 8,
                            child: IconButton(
                              icon: const Icon(Icons.close_rounded, color: Colors.white),
                              style: IconButton.styleFrom(
                                backgroundColor: Colors.black54,
                              ),
                              onPressed: _isLoading ? null : _removeImage,
                            ),
                          ),
                        ],
                      )
                          : Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.add_a_photo_outlined,
                            size: 48,
                            color: Colors.grey.shade500,
                          ),
                          const SizedBox(height: 12),
                          Text(
                            "Add Photo (Optional)",
                            style: TextStyle(color: Colors.grey.shade600),
                          ),
                        ],
                      ),
                    ),
                  ),

                  const SizedBox(height: 40),

                  // Submit button
                  SizedBox(
                    height: 56,
                    child: ElevatedButton.icon(
                      onPressed: _isLoading ? null : () {
                        if (_formKey.currentState!.validate()) {
                          _submitComplaint();
                        }
                      },
                      icon: _isLoading
                          ? const SizedBox.shrink()
                          : const Icon(Icons.send_rounded),
                      label: _isLoading
                          ? const SizedBox(
                        height: 20,
                        width: 20,
                        child: CircularProgressIndicator(
                          color: Colors.white,
                          strokeWidth: 2.5,
                        ),
                      )
                          : const Text(
                        "Submit Complaint",
                        style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
                      ),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.orange.shade700,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                        elevation: 3,
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