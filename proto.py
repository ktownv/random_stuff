import Tkinter
import datetime

blinker_mins = [13,14,28,29,43,44,58,59]

class Blinker:

	def __init__(self):
		self.win = Tkinter.Tk()
		self.canvas = Tkinter.Canvas(self.win, width = 205, height = 205)

		self.canvas.create_oval(80, 10, 120, 50, fill = 'white')
		self.canvas.create_oval(150, 80, 190, 120, fill = 'white')
		self.canvas.create_oval(80, 160, 120, 200, fill = 'white')
		self.canvas.create_oval(10, 80, 50, 120, fill = 'white')

		self.canvas.pack()

	def run(self):
		self.blinken_lights()
		Tkinter.mainloop()

	def blinken_lights(self):
		ts = datetime.datetime.now()
		did_blink = self.do_blink(ts)
		ts = datetime.datetime.now()

		if did_blink:
			rr = 1000 - (ts.microsecond/10000)
		else:
			rr = (((ts.minute / 15) + 1) * 15) - ts.minute - 2
			rr = (rr * 60 * 1000) - (ts.microsecond/1000)

		td = datetime.timedelta(milliseonds=rr)
		print 'will refresh in', rr, "at", ts+td
		self.win.after(rr, self.blinken_lights)


	def do_blink(self, ts):
		ms = ts.microsecond
		did_blink = False

		on_lights = (ts.minute / 15) + 1
		for i in range(1, on_lights+1):
			self.canvas.itemconfig(i, fill='#00FF00')

		for i in range(on_lights+1, 5):
			self.canvas.itemconfig(i, fill='white')

		if ts.minute in blinker_mins:

			light = (blinker_mins.index(ts.minute) / 2) + 2
			left = (((((light - 1) * 15 - ts.minute) * 60) - ts.second) * 1000) - ms/1000
			clr_bucket = int(round(left * (255/120000.)))

			h = hex(clr_bucket)[2:].upper()
			if len(h) == 1:
				h = '0' + h

			c = '#FF' + h + '00'

			print 'secs', light, ts.minute, ts.second, ms, left, clr_bucket, h, c
			if light == 5:
				light = 1

			if (left/1000) % 2:
				print 'color'
				self.canvas.itemconfig(light, fill=c)
			else:
				print 'white'

				self.canvas.itemconfig(light, fill='white')

			did_blink = True

		return did_blink




def main():

	b = Blinker()
	b.run()


if __name__ == '__main__':
	main()