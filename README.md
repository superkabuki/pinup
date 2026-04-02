# pinup
nudge nudge wink wink

```smalltalk
Successfully built pinup-1.0.3.tar.gz and pinup-1.0.3-py3-none-any.whl
twine upload dist/* --verbose
INFO     Using configuration from /home/a/.pypirc                              
Uploading distributions to https://upload.pypi.org/legacy/
INFO     dist/pinup-1.0.3-py3-none-any.whl (5.2 KB)                            
INFO     dist/pinup-1.0.3.tar.gz (4.2 KB)                                      
INFO     username set by command options                                       
INFO     password set from config file                                         
INFO     username: __token__                                                   
INFO     password: <hidden>                                                    
Uploading pinup-1.0.3-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.7/7.7 kB • 00:00 • ?
INFO     Response from https://upload.pypi.org/legacy/:                        
         400 Bad Request                                                       
INFO     <html>                                                                
          <head>                                                               
           <title>400 The name 'pinup' isn't allowed. See                      
         https://pypi.org/help/#project-name for more information.</title>     
          </head>                                                              
          <body>                                                               
           <h1>400 The name 'pinup' isn't allowed. See                         
         https://pypi.org/help/#project-name for more information.</h1>        
           The server could not comply with the request since it is either     
         malformed or otherwise incorrect.<br/><br/>                           
         The name &#x27;pinup&#x27; isn&#x27;t allowed. See                    
         https://pypi.org/help/#project-name for more information.             
                                                                               
                                                                               
          </body>                                                              
         </html>                                                               
ERROR    HTTPError: 400 Bad Request from https://upload.pypi.org/legacy/       
         Bad Request                                                           
make: *** [Makefile:33: upload] Error 1
a@fu:~/pinup$ 
```
