import asistent as js

def main ():
    message_voice = js.listenMicro()
    print(f'Im: {message_voice}')
    js.command_automatice(message_voice)

while True:
    main()

main()
