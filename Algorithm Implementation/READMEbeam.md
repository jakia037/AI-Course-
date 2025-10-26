# Beam Search Algorithm

## 🔹 How It Works
Beam Search explores a graph level by level but only keeps a limited number (beam width) of most promising nodes at each level, based on heuristic values.  
This reduces memory and computation compared to exhaustive search.

## 🔹 Applications
- AI Planning
- Machine Translation (NLP)
- Speech Recognition
- Game AI (limited-depth lookahead)

## 🔹 Complexity
- Time: O(b^d), where b = beam width, d = depth
- Space: O(b), since only the best `b` nodes are stored per level
