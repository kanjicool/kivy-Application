# Kivy Application Simple Paint by kanjicool


Kivy Application Simple Paint เป็นโปรแกรมวาดรูปง่ายๆที่เขียนด้วย Python โดยใช้ Library ที่ชื่อว่า Kivy มาพัฒนาแอพพลิเคชั่น 


# Table of Contents : สารบัญ 
- [การติดตั้ง kivy](#%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%20kivy)
- [วิธีการใช้งาน](##%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99)
- [อธิบาย Code](#%E0%B8%AD%E0%B8%98%E0%B8%B4%E0%B8%9A%E0%B8%B2%E0%B8%A2%20Code)
- [เครดิต](#%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%94%E0%B8%B4%E0%B8%95)




## การติดตั้ง kivy
``` bash
git clone https://github.com/kanjicool/kivy-Application.git

pip install kivy

```



## วิธีการใช้งาน
ง่ายมากแค่รันไฟล์ **app_paint.py** ก็เริ่มเล่นได้เลยอย่าลืมติดตั้ง kivy ด้วย
![Screenshot from 2024-01-14 20-46-02](https://github.com/kanjicool/kivy-Application/assets/144304593/f28c35da-5854-482e-a8e7-e166b2d4f224)

> ภาพผลการรันแอพพลิเคชั่น

## อธิบาย Code
**app_paint.py**

1. import module
```python
from  kivy.app  import  App

from  kivy.uix.widget  import  Widget

from  kivy.utils  import  get_color_from_hex

from  kivy.config  import  Config

from  kivy.uix.behaviors  import  ToggleButtonBehavior

from  kivy.uix.togglebutton  import  ToggleButton

from  kivy.graphics  import Color, Line
```
  
2. Class MyButton

```python
class  MyButton(ToggleButton):

	def  _do_press(self):

		if  self.state  ==  'normal':

			ToggleButtonBehavior._do_press(self)
```
  > เมธอด `_do_press()` ของคลาส `MyButton` จะเรียกเมธอด `_do_press()` ของคลาส `ToggleButton` เฉพาะเมื่อปุ่มอยู่ในสถานะ `normal` ช่วยให้สามารถกำหนดพฤติกรรมเพิ่มเติมสำหรับปุ่มได้โดยไม่ต้องเขียนโค้ดซ้ำ
3. Class PaintApp

```python
class  PaintApp(App):

	def  build(self):
	
		self.canvas_widget  =  CanvasWidget()

		self.canvas_widget.set_color(get_color_from_hex('#2980b9'))

		return  self.canvas_widget
```
 >บรรทัดนี้สร้างคลาสที่เรียกว่า `PaintApp` คลาสนี้สืบทอดมาจากคลาส `App` 
เมธอด `build()` ของคลาส `PaintApp` จะสร้างอินสแตนซ์ของคลาส `CanvasWidget` และตั้งค่าสีเริ่มต้นเป็นสี #2980b9 ซึ่งคือสีฟ้าอมเขียวเป็นสีเริ่มต้น
4. Class Widget  
```python
class  CanvasWidget(Widget):

	line_width  =  2 # ตั้งค่าความกว้างเส้นเริ่มต้นเป็น 2

	mode  =  ''

	def  set_mode(self, mode):

		self.mode  =  mode

		if  mode  ==  'pencil':

		self.canvas.add(Color(*self.last_color))# กำหนดสีปัจจุบัน ใช้สำหรับวาดด้วยเส้นดินสอ


		self.line_width  =  2  # Set ค่าขนาดเส้นเริ่มต้นของดินสอ

		elif  mode  ==  'eraser':

		self.canvas.add(Color(1, 1, 1, .9)) # กำหนดสีกึ่งโปร่งใสสำหรับยางลบ

		self.line_width  =  10 # Set ค่าขนาดของยางลบ

	def  set_color(self, new_color):

		self.last_color  =  new_color # บันทึกสีใหม่ที่เราเลือก

		self.canvas.add(Color(*new_color)) # กำหนดสีปัจจุบันที่ใช้ในการวาด

	  

	def  on_touch_down(self, touch): # การตอบสนองต่อการสัมผัสหน้าจอ (เริ่มวาด)

		if  Widget.on_touch_down(self, touch): #ตรวจสอบการโต้ตอบกับวิดเจ็ตอื่นๆ


		return  True

		if  self.mode  ==  'pencil':

		touch.ud['line_width'] =  self.line_width # บันทึกความกว้างเส้นปัจจุบัน


		  

		with  self.canvas:

		touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=self.line_width)

	def  on_touch_move(self, touch): # การตอบสนองต่อการสัมผัสหน้าจอ (เคลื่อนที่ขณะวาด)

		if  'current_line'  in  touch.ud: # ตรวจสอบว่ามีเส้นที่กำลังวาดอยู่หรือไม่


			if  self.mode  ==  'eraser':

				lw  =  self.line_width  # ใช้ขนาดที่กำหนดไว้ของยางลบ

			else:

				lw  =  self.line_width  # ใช้ขนาดของเส้นที่เก็บไว้สำหรับโหมดอื่น

				touch.ud['current_line'].points += (touch.x, touch.y)

				touch.ud['current_line'].width =  lw

	def  clear_canvas(self): # ฟังก์ชันล้างแคนวาส

		saved  =  self.children[:] # บันทึกวิดเจ็ตอื่นๆ บนแคนวาส


		self.clear_widgets() # ล้างวิดเจ็ตทั้งหมด


		self.canvas.clear() # ล้างเส้นทั้งหมด

		for  widget  in  saved:

			self.add_widget(widget) # เพิ่มวิดเจ็ตที่บันทึกไว้กลับเข้าไป


		self.set_color(self.last_color) # กำหนดสีปัจจุบันอีกครั้ง


	  

	def  set_line_width(self, line_width  =  'Normal'): # กำหนดขนาดเส้น

			self.line_width  = {'Thin' : 1, 'Normal' : 2, 'Thick' : 4}[line_width]

	  

	def  undo(self): # ฟังก์ชันย้อนการทำงาน

		if  self.canvas.children: # ตรวจสอบว่ามีเส้นที่สามารถย้อนได้หรือไม่


		self.canvas.remove(self.canvas.children[-1]) # ลบเส้นที่วาดล่าสุด

```
 >ตัวแปร `line_width` เก็บความกว้างเส้นเริ่มต้นสำหรับเครื่องมือวาดภาพ
ตัวแปร `mode` เก็บโหมดการวาดภาพปัจจุบัน ซึ่งอาจเป็น "ดินสอ" หรือ "ยางลบ"
  5. แสดงผล
```python
if  __name__  ==  "__main__":

	from  kivy.core.window  import  Window

	Config.set('graphics', 'width', '960')

	Config.set('graphics', 'height', '540')

	Window.clearcolor =  get_color_from_hex('#ffffff')

	PaintApp().run()

```
**paint.kv**
1. กำหนดเวอร์ชัน kivy และ import ฟังก์ชันสำหรับแปลงสี
``` python
#:kivy 1.0.9

#:import C kivy.utils.get_color_from_hex

# from kivy.utils import get_color_froom_hex as C
```
  2. สร้างคลาสปุ่มแบบกำหนดเอง
```python
<MyButton>

background_normal :  'sigma_cat.png' # ใส่รูปภาพที่ต้องการ

background_normal :  'sigma_cat.png'

border : (3,3,3,3) # กำหนดเส้นขอบ
```
  3 .สร้างปุ่มสี
```python
<ColorButton@MyButton>

group :  'color'

on_release: app.canvas_widget.set_color(self.background_color)
```
  4. สร้างปุ่มเลือกความกว้างของเส้น
```python
<LineWidthButton@MyButton>

group :  'linewidth'

background_color : C('#808080')

on_release: app.canvas_widget.set_line_width(self.text)
```
  5. กำหนดเลย์เอาต์สำหรับ CanvasWidget
```python
<CanvasWidget>

Button: # Clear

text:'Clear'

font_size:20

right: root.right

top:root.top

width:100

height:60

background_normal :  '/home/kunanon/kanjicool2077/1-2/241-152 BAISD-2-66/kiwy_app/kivy-Application/app/template/clear_buuton(2).png' 

background_down :  '/home/kunanon/kanjicool2077/1-2/241-152 BAISD-2-66/kiwy_app/kivy-Application/app/template/clear_buuton(1).png'

border: (2,2,2,2)

on_release: root.clear_canvas()

  

Button: # ปุ่ม Undo

text:  'Undo'

font_size:  20

right: root.right

top : root.top - self.height

width:100

height:60

border: (2, 2, 2, 2)

on_release: root.undo()

  

Button: # ปุ่มดินสอ

text:  'Pencil'

font_size:  20

right: root.right

top: root.top - self.height *2  # Position below Clear button

width:  100

height:  60

# background_normal: 'pencil_button.png' # Replace with your image

# background_down: 'pencil_button.png'

border: (2, 2, 2, 2)

on_release: root.set_mode('pencil') # Bind to the s

  

Button: # ปุ่มยางลบ

text:  'Eraser'

font_size:  20

right: root.right

top: root.top - self.height * 4  # Position below Pencil button

width:  100

height:  60

border: (2, 2, 2, 2)

on_release: root.set_mode('eraser') # Bind to the eraser mode

  

BoxLayout: 

orientation:'vertical'

padding:2

spacing:2

x :  0

top: root.top

width:  80

height :  120

  

LineWidthButton: # ขนาดเส้น

text :  'Thin'

LineWidthButton:

text :  'Normal'

LineWidthButton:

text :  'Thick'

  

BoxLayout:

orientation:  'horizontal'

padding :  2

spacing :  2

x:  0

y:  0

width : root.width

height:  40

  

ColorButton: # ปุ่มสี

background_color: C('#2980b9')

state:  'down'

  

ColorButton:

background_color: C('#16a085')

  

ColorButton:

background_color: C('#27ae60')

  

ColorButton:

background_color: C('#f39c12')

  

ColorButton:

background_color: C('#d35400')

  

ColorButton:

background_color: C('#c0392b')

  

ColorButton:

background_color: C('#8e44ad')

ColorButton:

background_color: C('#bdc3c7')

  

ColorButton:

background_color: C('#7f8c8d')

  

ColorButton:

background_color: C('#2c3e50')

  

ColorButton:

background_color: C('#3498db')

  

ColorButton:

background_color: C('#1abc9c')

  

ColorButton:

background_color: C('#2ecc71')

  

ColorButton:

background_color: C('#f1c40f')

  

ColorButton:

background_color: C('#e67e22')

  

ColorButton:

background_color: C('#e74c3c')

  

ColorButton:

background_color: C('#9b59b6')

  

ColorButton:

background_color: C('#ecf0f1')

  

ColorButton:

background_color: C('#95a5a6')

  

ColorButton:

background_color: C('#34495e')
```
>-   ปุ่ม Clear: ล้างแคนวาส
>-   ปุ่ม Undo: ย้อนกลับการทำงาน
>-   ปุ่ม Pencil: ตั้งค่าโหมดเป็น 'pencil'
>-   ปุ่ม Eraser: ตั้งค่าโหมดเป็น 'eraser'
>-   กล่อง BoxLayout แนวตั้งสำหรับปุ่มความกว้างเส้น
>-   กล่อง BoxLayout แนวนอนสำหรับปุ่มสี
## เครดิต

kanjicool
6610110034 นายคุณานนต์ หนูแสง
## 


