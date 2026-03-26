// import 'package:flutter/material.dart';
// import 'package:shared_preferences/shared_preferences.dart';
//
// import 'login.dart';
//
// void main() {
//   runApp(const MyApp());
// }
//
// class MyApp extends StatelessWidget {
//   const MyApp({super.key});
//
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Flutter Demo',
//       theme: ThemeData(
//         colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
//         useMaterial3: true,
//       ),
//       home: const MyHomePage(title: 'IP Page'),
//     );
//   }
// }
//
// class MyHomePage extends StatefulWidget {
//   const MyHomePage({super.key, required this.title});
//
//   final String title;
//
//   @override
//   State<MyHomePage> createState() => _MyHomePageState();
// }
//
// class _MyHomePageState extends State<MyHomePage> {
//   // ✅ Create a TextEditingController
//   final TextEditingController _textController = TextEditingController();
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         backgroundColor: Theme.of(context).colorScheme.inversePrimary,
//         title: Text(widget.title),
//       ),
//       body: Center(
//         child: Padding(
//           padding: const EdgeInsets.all(16.0),
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.center,
//             children: <Widget>[
//               // ✅ TextField with controller
//               TextField(
//                 controller: _textController,
//                 decoration: const InputDecoration(
//                   labelText: 'Enter Your Ip Address',
//                   border: OutlineInputBorder(),
//                 ),
//               ),
//               const SizedBox(height: 20),
//               // ✅ ElevatedButton
//               ElevatedButton(
//                 onPressed: () {
//                   _send_data();
//                 },
//                 child: const Text('Submit'),
//               ),
//             ],
//           ),
//         ),
//       ),
//     );
//   }
//
//   void _send_data() async{
//     SharedPreferences sh = await SharedPreferences.getInstance();
//     sh.setString('url', 'http://${_textController.text}:8000/myapp');
//     sh.setString('img_url', 'http://${_textController.text}:8000');
//     Navigator.push(context, MaterialPageRoute(
//       // builder: (context) => MyLoginPage(title: "Login"),));
//       builder: (context) =>const LoginPage(),));
//
//   }
//
// }
import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'login.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ServerConfigPage(),
  ));
}

class ServerConfigPage extends StatefulWidget {
  const ServerConfigPage({super.key});

  @override
  State<ServerConfigPage> createState() => _ServerConfigPageState();
}

class _ServerConfigPageState extends State<ServerConfigPage> {
  final _formKey = GlobalKey<FormState>();
  final _ipController = TextEditingController();
  bool _isLoading = false;
  String? _savedIp;

  @override
  void initState() {
    super.initState();
    _loadSavedIp();
  }

  Future<void> _loadSavedIp() async {
    final sh = await SharedPreferences.getInstance();
    final saved = sh.getString('server_ip');
    if (saved != null && saved.isNotEmpty) {
      setState(() {
        _savedIp = saved;
        _ipController.text = saved;
      });
    }
  }

  Future<void> _saveAndContinue() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      final ip = _ipController.text.trim();
      final baseUrl = 'http://$ip:8000/myapp';
      final imgBase = 'http://$ip:8000';

      final sh = await SharedPreferences.getInstance();
      await sh.setString('url', baseUrl);
      await sh.setString('img_url', imgBase);
      await sh.setString('server_ip', ip); // remember for next time

      Fluttertoast.showToast(
        msg: "Server configured successfully",
        backgroundColor: Colors.green.shade700,
        textColor: Colors.white,
      );

      if (mounted) {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (_) => const LoginPage()),
        );
      }
    } catch (e) {
      Fluttertoast.showToast(
        msg: "Error saving configuration: $e",
        backgroundColor: Colors.red.shade700,
      );
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
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Color(0xFF667EEA), Color(0xFF764BA2)],
          ),
        ),
        child: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 32),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    // Header / Illustration
                    const Icon(
                      Icons.dns_rounded,
                      size: 90,
                      color: Colors.white,
                    ),
                    const SizedBox(height: 24),

                    const Text(
                      "Server Setup",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 32,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      "Enter your backend server IP to continue",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 16,
                        color: Colors.white.withOpacity(0.9),
                      ),
                    ),

                    const SizedBox(height: 48),

                    // Card with form
                    Container(
                      padding: const EdgeInsets.all(28),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(28),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.18),
                            blurRadius: 24,
                            offset: const Offset(0, 12),
                          ),
                        ],
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          // Saved IP hint
                          if (_savedIp != null) ...[
                            Text(
                              "Last used: $_savedIp",
                              style: TextStyle(
                                fontSize: 13,
                                color: Colors.grey.shade600,
                              ),
                            ),
                            const SizedBox(height: 8),
                          ],

                          TextFormField(
                            controller: _ipController,
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.done,
                            decoration: InputDecoration(
                              labelText: "Server IP Address",
                              hintText: "192.168.1.100 or 10.0.2.2",
                              prefixIcon: const Icon(Icons.computer_rounded),
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(16),
                                borderSide: BorderSide.none,
                              ),
                              filled: true,
                              fillColor: const Color(0xFFF7FAFC),
                              contentPadding: const EdgeInsets.symmetric(
                                vertical: 16,
                                horizontal: 20,
                              ),
                            ),
                            validator: (value) {
                              if (value == null || value.trim().isEmpty) {
                                return 'Please enter the server IP';
                              }
                              // Very basic IP-like validation
                              final trimmed = value.trim();
                              if (!RegExp(r'^(\d{1,3}\.){3}\d{1,3}$').hasMatch(trimmed) &&
                                  trimmed != 'localhost') {
                                return 'Enter a valid IP (e.g. 192.168.1.100)';
                              }
                              return null;
                            },
                          ),

                          const SizedBox(height: 32),

                          SizedBox(
                            height: 56,
                            width: double.infinity,
                            child: ElevatedButton.icon(
                              onPressed: _isLoading ? null : _saveAndContinue,
                              icon: _isLoading
                                  ? const SizedBox.shrink()
                                  : const Icon(Icons.arrow_forward_rounded),
                              label: _isLoading
                                  ? const SizedBox(
                                height: 24,
                                width: 24,
                                child: CircularProgressIndicator(
                                  color: Colors.white,
                                  strokeWidth: 2.5,
                                ),
                              )
                                  : const Text(
                                "Connect & Continue",
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                              style: ElevatedButton.styleFrom(
                                backgroundColor: const Color(0xFF5E72E4),
                                foregroundColor: Colors.white,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(16),
                                ),
                                elevation: 2,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 32),

                    // Extra help text
                    Center(
                      child: Text(
                        "Make sure your server is running on port 8000",
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.85),
                          fontSize: 14,
                        ),
                      ),
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
