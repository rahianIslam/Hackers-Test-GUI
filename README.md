# a5-hackers_t-test_gui
Create a graphical user interface to compute a hacker's t-test.

__Due: Tuesday March 31, noon, code on github, HTTPS link on D2L__

Author: Rahian Islam

# Problem statement
We would like to compute whether measurements of two groups are different. As an example, we could ask if students that had prior Python experience did better in this course midterm, than students that did not have this experience. The computation needed is called a [t-test](https://en.wikipedia.org/wiki/Student's_t-test).

While there are formulae and a process to carry out a student t-test, the goal of this assignment to implement a hacker's version as presented in this video [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA) (start at ~8min). A github user prepared a [Jupyter notebook](https://github.com/croach/statistics-for-hackers/blob/master/statistics-for-hackers.ipynb) with Python code for what is presented.

As explained in the video, the hacker's t-test assumes that measurements of Group A and Group B come from the same parent group, i.e. are the same. All measurements are pooled, then, repeatably, measurements are randomly assigned to Group A and Group B. The difference in means between the groups is calculated and stored. The percentage of simulated group differences larger than the original group difference indicates the significance value (p-value).

You will build a graphical user interface with Python and tkinter that:
1. Provides two text fields to enter measurements for two groups.
2. Contains a button to start simulation (10000 iterations) and displaying the resulting p-value in a copy-paste'able widget.
3. Includes a Matplotlib plotting canvas to display the simulation histogram along with measured difference and p-value.
4. Alerts the user with a pop-up message about errors in data conversion or simulation.
5. Test your GUI with the Sneetches data presented in the video.

Optionally, you might consider including:
- Adding a widget to select the number of iterations.
- Add widgets and logic to compare simulation to `statsmodel.t_test`.
- Add a progressbar indicating simulation progress.
- Move the simulation into a thread in order for the GUI not to block.
- Extend the t-test from handling only 'larger' to handling 'larger', 'smaller' and 'two-sided' alternatives.

# What to do
Watch the video [Jake Vanderplas - Statistics for Hackers - PyCon 2016](https://www.youtube.com/watch?v=Iq9DzN6mvYA) (start at ~8min). Study the code in [Jupyter notebook](https://github.com/croach/statistics-for-hackers/blob/master/statistics-for-hackers.ipynb).

Design and implement a graphical user interface with the mandatory elements 1. - 5. outlined above. You may re-use the code from the Jupyter notebook. Save your code in a file `a5-hackers_t-test_gui.py`. A possible implementation could look like this:

![Screenshot of example GUI](hackers_t-test_gui_screenshot.png)

Follow the [Style Guide](StyleGuide.md), and use git and github to track your changes.

Edit `README.md` (this file) and include instructions on how to run your program and expected outputs (screenshots) in the _How to run this program_ section below. Make sure to describe how the data needs to be formatted, e.g. one measurement per line, space separated, etc. Use the Sneetches data from the video (available in the Jupyter notebook) as sample data. 

Make sure final version of your code `a5-hackers_t-test_gui.py` and updated `README.md` with referenced files (screenshots etc.) are committed to git and pushed to github. 

# How to run this program
_Add your instructions and screenshot here_