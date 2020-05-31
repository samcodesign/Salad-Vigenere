import paperclip, socketserver
from secret import flag	


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def chall(req):
	Key = 'ASIMOV'
	Mode = 'encrypt'

	if Mode == 'encrypt':
		translated = encryptMessage(Key, flag)

	req.sendall(b'%sed message:' % (Mode.title()))
	req.sendall(translated)
	paperclip.copy(translated)
	req.sendall(b'The message has been copied to the clipboard.')



def encryptMessage(key, message):
	return translateMessage(key, message, 'encrypt')


def translateMessage(key, message, mode):
	translated = []
	keyIndex = 0
	key = key.upper()

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			if mode == 'encrypt':
				num += LETTERS.find(key[keyIndex])

			num %= len(LETTERS)
			if symbol.isupper():
				translated.append(LETTERS[num])
			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(symbol)

	return ''.join(translated)


class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
    	chall(self.request)


if __name__ == '__main__':
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        server = socketserver.ThreadingTCPServer(('0.0.0.0', 8080), TaskHandler)
        server.serve_forever()
 		
