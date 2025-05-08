📚 Knowledge Graph Builder
This Python script creates a customized knowledge graph from a CSV file, drawing connections between inner nodes and outer ring regions with user-defined connection strengths.
The final output is a publication-quality graph saved automatically as a PNG image (knowledge_graph.png).
 
✨ Features
•	Flexible number of inner nodes and outer regions
•	Thickness of connecting lines based on input strength values
•	Colored inner nodes and outer regions for easy mapping
•	Separate legends for nodes and outer regions
•	Clean, professional layout using matplotlib
•	Automatic saving as high-resolution PNG
•	Easy to adapt for publication, reports, or presentations
 
📈 Example Diagram
(Insert a sample generated image here once you run the script!)
 
 
📂 How It Works
1.	Prepare your CSV file:
The first column should be the node names.
Each subsequent column corresponds to an outer region and contains connection strengths.
Example CSV format:
NodeName	Region1	Region2	Region3	Region4	Region5
Node A	8	7	7	6	7
Node B	5	6	4	5	6
2.	Run the script:
bash
Copy
python knowledge_graph_builder.py
3.	Enter the path to your CSV file when prompted.
4.	View the generated graph and find knowledge_graph.png saved in the working directory!
 
🛠️ Requirements
•	Python 3.7+
•	Packages:
o	matplotlib
o	pandas
o	numpy
Install required packages:
bash
Copy
pip install matplotlib pandas numpy
 
📜 License
This project is released under the MIT License.
 