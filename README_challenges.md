# Robot Challenges
## Background of line following robot:
1. Below are some of the earliest maze solver robots.</br>
http://cyberneticzoo.com/tag/amazing-micromouse-maze-contest/</br>
http://cyberneticzoo.com/wp-content/uploads/2011/08/Emily-Popular-Electronics-Mar-1962.pdf
2. Maze solver is actually SLAM(simultaneous localization and mapping). However we are not going to do mapping in the assignment(encoder is required). We will only solve localized shortest path.

## Challenges
1. Straight line 
2. Straight line to and fro</br>
[![Watch the video](https://img.youtube.com/vi/e3iG1YwLLdQ/0.jpg)](https://youtu.be/e3iG1YwLLdQ)
3. T - junctions to and fro</br>
[![Watch the video](https://img.youtube.com/vi/7VvkeIZoFew/0.jpg)](https://youtu.be/7VvkeIZoFew)
4. maze solving
5. maze shortest path(mapping)
## Note for challenges 1 and 2:
<img src="https://github.com/skyap/alphabot2/blob/master/images/to.jpg" width="400"></br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/to_and_fro.jpg" width="400"></br>
1. Line tracker sensors return analog readings. You need to convert this to digital for decision making.</br>
2. You need to understand what your sensors' logic in different situation:</br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/logic1.jpg" width="400">

## Note for challenge 3
<img src="https://github.com/skyap/alphabot2/blob/master/images/t-junctions.jpg" width="400"></br>
1. Simple straight line with branches 
2. What your sensors' logic at junction?

## Note and rules for challenges 4 and 5:
1. Simply connected line maze will be used (no loops)
2. Black line on a while or bright background.
3. Each line maze has a start and finish point. The robot is expected to follow the lines and find it's way from start to finish. No mark is giving based on finishing time.
4. 8 maze possibilities
<img src="https://github.com/skyap/alphabot2/blob/master/images/maze1.jpg" width="400">
5. Below will not be implemented
<img src="https://github.com/skyap/alphabot2/blob/master/images/acute_turn.jpg" width="400">
6. line will be at least visible by one sensor all the time</br>
7. This is the examples of line maze(with left hand rule)
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1.jpg" width="400">
8. This is the example of line maze shortest path from start to finish
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1-shorest_path.jpg" width="400">
9. This is the example of line maze shortest path from finish to start 
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1-shorest_path2.jpg" width="400">