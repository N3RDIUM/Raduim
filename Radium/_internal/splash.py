from _typebase import *

class Splash(HTMLPage):
    def __init__(self):
        self.html = '''
           <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8"/>        
                    <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
                </head>
                <body> <h2 id="header">RADIUM - LOADING</h2> </body>
                <script>
                    var Radium;
                    new QWebChannel(qt.webChannelTransport, function (channel) {
                        Radium = channel.objects.Radium;
                    });

                    document.getElementById("header").addEventListener("click", function(){
                        Radium.run("print('You found an easter egg!')");
                    });
                </script>
            </html>
        '''
        super().__init__(self.html)
