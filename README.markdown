# 🎨 Image Drawing & Filtering Tool with Tkinter and PIL

A simple, fun, and powerful Python application for drawing, editing, and applying filters to images using **Tkinter** and **PIL (Pillow)**! 🎉  
**Author:** Arshia  

---

## 🌟 Introduction to the Application

The *Image Drawing & Filtering Tool* lets you upload images, unleash your creativity with tools like freehand drawing, rectangles, lines, and text, apply cool filters, and save your masterpiece! 🖼️ This program features a simple and user-friendly graphical user interface (GUI), making it perfect for quick edits or creative projects! 🚀  

---

## ✨ Key Features of the Application

This app is packed with amazing features that turn working with it into a delightful experience:  

- **🎞️ Image Loading**: Click "Add Image" to upload any image you love onto the canvas!  
- **🖌️ Professional Drawing Tools**:  
  - *Free Draw* ✍️: Draw anything you want with your mouse!  
  - *Rectangle Tool* 🔲: Create rectangles with customizable outlines.  
  - *Line Tool* ➖: Draw straight and precise lines.  
  - *Text Tool* 📝: Add any text with your preferred color and size.  
- **🎨 Exciting Customization**:  
  - Change the pen color with a cool color chooser dialog! 🌈  
  - Adjust pen size between 3, 5, or 7 pixels! 📏  
- **🖼️ Cool Filters**: Try out effects like Black and White, Blur, Emboss, Sharpen, and Smooth!  
- **↩️ Undo & Clear**: Use "Undo" to revert your last action or "Clear" to reset the canvas like new! 🧹  
- **💾 Easy Saving**: Save your edited image as a PNG file and show it off to everyone!  

---

## 📸 Screenshots of the Application

1. **Loaded Image** 🎞️:  
   ![Loaded Image](screenshots/screenshot2.png)  
   *A beautiful cloud image loaded onto the canvas!*  

2. **Pen Color Selection** 🌈:  
   ![Color Selection](screenshots/screenshot3.png)  
   *Check out the color chooser dialog for the pen!*  

3. **Drawing and Annotations** ✍️:  
   ![Annotations](screenshots/screenshot4.png)  
   *A heatmap with freehand drawings, a rectangle, and cool lines!*  

---

## 🚀 Quick Installation and Setup

### Prerequisites  
- **🐍 Python 3**: Make sure you have Python 3.x on your system!  
- **🖥️ Tkinter**: Comes pre-installed with Python, no extra setup needed.  
- **🖼️ Pillow (PIL)**: Essential for the magic of image processing!  

### Installation Steps  
1. If you don’t have Pillow, install it with this command:  
   ```bash  
   pip install pillow  
   ```  
2. Download the main app file and navigate to its folder.  
3. Run the program with this command:  
   ```bash  
   python image_drawing_tool.py  
   ```  
   Now you’re ready to get creative! 🎨  

---

## 🖌️ How to Use It?

1. **Launch the Application** 🚀: Execute the script to open the GUI.  
2. **Upload an Image** 🎞️: Click "Add Image" and select an image from your computer.  
3. **Start Drawing and Editing** ✍️:  
   - Use the "Free Draw", "Rectangle Tool", "Line Tool", or "Text Tool" buttons.  
   - Click "Change Color" to switch pen colors. 🌈  
   - Adjust the pen size with radio buttons (3, 5, or 7). 📏  
   - Type text in the text field and click on the canvas to place it (when the Text Tool is active).  
4. **Apply Filters** 🖼️: Pick a filter from the "Select Filter" dropdown, like Blur or Sharpen.  
5. **Undo or Clear** ↩️: Use "Undo" to revert the last change or "Clear" to wipe everything.  
6. **Save Your Masterpiece** 💾: Click "Save Image" to save your image as a PNG!  

---

## 🖥️ Details of the User Interface (GUI)

- **Left Sidebar (Toolbar)** 🛠️:  
  - Background color: Vibrant turquoise (#47CDD2).  
  - Includes tool buttons, a text entry field, pen size options, and a filter dropdown.  
- **Main Canvas** 🎨:  
  - Size: 900x700 pixels, plenty of space for creativity!  
  - Where all drawing and editing takes place.  
- **Main Window** 🖼️:  
  - Title: "Image Drawing Tool".  
  - Size: 1100x700 pixels, spacious and comfy!  

---

## 📦 Used Libraries

- **🐍 Python 3**: The foundation that ties everything together!  
- **🖥️ Tkinter**: Python’s standard library for building graphical user interfaces, simple yet powerful!  
- **🖼️ Pillow (PIL)**: The heart of image processing in this app! It handles loading, editing, and filtering images.  

---

## 🧠 Algorithms and the Magic Behind the Scenes

- **🎨 Free Draw**:  
  - With every mouse move, tiny circles are drawn and connected to create a smooth, freehand line!  
  - Algorithm: Continuously tracks mouse coordinates and connects points to form lines.  
- **🔲 Rectangle and Line Drawing**:  
  - Clicking and dragging shows a temporary shape, which finalizes when you release the mouse!  
  - Algorithm: Captures start and end coordinates to draw the shape accurately.  
- **✍️ Text Tool**:  
  - Takes text from the entry field and places it on the canvas with the chosen font and color upon clicking.  
- **🖼️ Filters**:  
  - Uses Pillow’s built-in functions like `ImageFilter.BLUR` and `ImageFilter.SHARPEN` for fast, high-quality effects!  
- **↩️ Undo Feature**:  
  - Each change (like drawing a line or rectangle) is stored in a stack (Stack), and Undo removes the last item.  
- **🧹 Clearing the Canvas**:  
  - Resets the entire canvas and reloads the initial image (if present).  

---

## 🎨 Exciting Graphical Options

- **🌈 Pen Color Selection**:  
  - A standard Tkinter dialog lets you pick any color you desire for the pen!  
  - Powered by `tkinter.colorchooser`, offering a full color palette.  
- **📏 Pen Size Adjustment**:  
  - Three options (3, 5, 7 pixels) available via radio buttons!  
  - Adjusts the thickness of freehand circles and line/rectangle outlines.  
- **🖋️ Text Font**:  
  - Uses the "Arial" font, clean and readable!  
  - Font size scales with the pen size for a cohesive look.  
- **🖼️ Image Resizing**:  
  - Uploaded images automatically resize to fit the canvas (900x700) while preserving quality!  
  - Utilizes the `Image.resize` method from Pillow.  

---

## 💡 Useful Tips for Someone Viewing the Code

- **🖱️ How to Draw?**:  
  - For freehand, hold the mouse and drag. For rectangles and lines, click, drag, and release!  
- **📝 Adding Text**:  
  - Select the Text Tool first, type in the text field, and click on the canvas to place it.  
- **🎨 Quick Color Change**:  
  - Hit "Change Color" anytime to pick a new shade—super easy!  
- **💾 Saving**:  
  - After editing, always click "Save Image" to preserve your hard work!  
- **⚠️ Important Note**:  
  - If you try to save without loading an image, it’ll show an error saying "Load an image first!"  
- **🧠 Understanding the Code**:  
  - The code is clean and modular; each tool and feature is explained in its section, making it easy to modify!  

---

## 🛠️ Ideas to Enhance the Application

- **🆕 More Tools**: Add circle, oval, or polygon tools!  
- **🎨 Advanced Filters**: Try brightness, contrast, or even color filters.  
- **🖌️ Diverse Pens**: Include more thickness options or dotted pen styles.  
- **🎨 UI Themes**: Allow changing the sidebar or canvas color.  
- **🖼️ More Formats**: Add support for saving as JPEG or BMP!  

---

## 📜 Project License

This application is released under the **MIT License**. You’re free to use it, modify it, and work with it however you like! 😊  

---

## 📧 Contact Me

Got a question or suggestion? I’d love to hear from you:  
- **Author**: Arshia  
- **Email**: [Arshia82sbn@gmail.com](mailto:arshiasbn82@gmail.com)  

Hope this tool brings you tons of fun and creativity! 🎉 Now go create your masterpiece! 🖼️
