## Faster Python Programs - Measure, don't Guess
[Mike Müller](https://us.pycon.org/2018/speaker/profile/314/)  
[Wednesday 1:20 p.m.–4:40 p.m. in Room 22](https://us.pycon.org/2018/schedule/presentation/61/)

### Description
Optimization can often help to make Python programs faster or use less memory. Developing a strategy, establishing solid measuring and visualization techniques as well as knowing about algorithmic basics and datastructures are the foundation for a successful optimization. The tutorial will cover these topics. Examples will give you a hands-on experience on how to approach efficiently.

Python is a great language. But it can be slow compared to other languages for certain types of tasks. If applied appropriately, optimization may reduce program runtime or memory consumption considerably. But this often comes at a price. Optimization can be time consuming and the optimized program may be more complicated. This, in turn, means more maintenance effort. How do you find out if it is worthwhile to optimize your program? Where should you start?

This tutorial will help you to answer these questions. You will learn how to find an optimization strategy based on quantitative and objective criteria. You will experience that one's gut feeling what to optimize is often wrong.

The solution to this problem is: „Measure, Measure, and Measure!“. You will learn how to measure program run times as well as profile CPU and memory. There are great tools available. You will learn how to use some of them. Measuring is not easy because, by definition, as soon as you start to measure, you influence your system. Keeping this impact as small as possible is important. Therefore, we will cover different measuring techniques.

Furthermore, we will look at algorithmic improvements. You will see that the right data structure for the job can make a big difference. Finally, you will learn about different caching techniques.

### Software Requirements
You will need Python 2.7 or 3.6 installed on your laptop. Python 2.6 or 3.4/3.5 should also work. Python 3.x is strongly preferred. If released, we will use Python 3.7.

#### Jupyter Notebook
I will use a Jupyter Notebook for the tutorial because it makes a very good teaching tool. You are welcome to use the setup you prefer, i.e editor, IDE, REPL. If you also like to use a Jupyter Notebook, I recommend conda for easy installation. Similarly to virtualenv, conda allows creating isolated environments but allows binary installs for all platforms.

There are two ways to install Jupyter via conda:

Use Minconda. This is a small install and (after you installed it) you can use the command conda to create an environment: conda create -n pycon2018 python=3.6 Now you can change into this environment: source activate pycon2018. The prompt should change to (pycon2018). Now you can inst

#### Working witch conda environments
After creating a new environment, the system might still work with some stale settings. Even when the command which tells you that you are using an executable from your environment, this might actually not be the case. If you see strange behavior using a command line tool in your environment, use hash -r and try again.

### Tools
You can install these with pip (in the active conda environment with conda):
 - [SnakeViz](http://jiffyclub.github.io/snakeviz/)
 - [line_profiler](https://pypi.python.org/pypi/line_profiler/)
 - [Pympler](https://pypi.python.org/pypi/Pympler)
 - [memory_profiler](https://pypi.python.org/pypi/memory_profiler)

### Notes
 - Bounds: memory, io, cpu
 - Balance speed of development and speed of programming executions
 - Find bottlenecks by profiling, measuring
 -  
