# 🍅 **PomoBlocker** 🍅

## Project Description
It can be difficult to focus on tasks, especially with websites like YouTube and Twitter a click away. This was the core motivation behind developing Pomoblocker.

PomoBlocker is a Python GUI application built with Tkinter & [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). This application essentially combines the [Pomodoro productivity technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) with a website blocker. The website blocker works by adding inputted websites to the Windows hosts file. 

### Features
Users can...
- set custom Pomodoro times for the three cycles (work period, short break period, long break period)
- block websites during any of these three cycles
- set preferred notification settings that notify them of a cycle ending

### Features to implement in the future...
- [ ] Ability for users to login to save their custom settings using SQLite
- [ ] Linux/Mac compatability
- [ ] Block applications by editing the Windows registry

### Personal challenges
As this was my first personal project, I faced many challenges developing this application. The main challenges included structuring the application (ensuring users "progress" smoothly through the app), user interface, and properly using OOP to organize GUI code/logic. This being said, developing an app from the ground up has greatly solidified my skills in these areas. Some solutions I used to overcome these blocks included hand drawing multiple possible user interfaces, studying existing OOP code behind GUIs, and writing test cases for the app.

### Sample screenshots
- Settings - Set custom times page:

![Image 1](/res/settings_sc1.png)
