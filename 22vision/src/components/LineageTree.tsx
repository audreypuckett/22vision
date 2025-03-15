import React, { useEffect, useRef, useState } from "react";
import * as d3 from "d3";

// Define the King data structure
interface KingNode {
    name: string;
    reign: string;
    nation: string;
    children?: KingNode[];
}

const LineageTree: React.FC = () => {
    const [data, setData] = useState<KingNode | null>(null);
    const svgRef = useRef<SVGSVGElement | null>(null);

    // Fetch lineage data from API
    useEffect(() => {
        fetch("http://localhost:8000/kings")
            .then(response => response.json())
            .then((data: KingNode) => {
                setData(data);  // ✅ Store data
            })
            .catch(error => console.error("Error fetching lineage data:", error));
    }, []);

    useEffect(() => {
        if (data) {
            renderTree(data);  // ✅ Use data when it changes
        }
    }, [data]);  // 🔥 Runs only when data is updated

    const renderTree = (treeData: KingNode) => {
        if (!treeData || !svgRef.current) return;

        const width = 800;
        const height = 500;

        // Select and configure the SVG
        const svg = d3.select(svgRef.current)
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", [-width / 2, -height / 2, width, height]) // Centered view
            .style("background", "#f8f9fa"); // Light background for contrast

        svg.selectAll("*").remove(); // Clear previous elements

        // ✅ Create a group (`g`) to apply transformations
        const g = svg.append("g").attr("transform", `translate(${width / 4}, ${height / 2})`);

        // Convert data into a hierarchical structure
        const root = d3.hierarchy(treeData);

        // ✅ Swap width & height to make it horizontal
        const treeLayout = d3.tree<KingNode>().size([height - 200, width - 300]);
        treeLayout(root); // ✅ Ensures x and y positions are assigned

        console.log("Tree Nodes with Positions:", root.descendants().map(d => ({ name: d.data.name, x: d.x, y: d.y }))); // Debugging

        // ✅ Swap x and y coordinates to make the tree horizontal
        g.selectAll("line")
            .data(root.links())
            .enter()
            .append("line")
            .attr("x1", d => d.source.y ?? 0) // Swap x/y
            .attr("y1", d => d.source.x ?? 0)
            .attr("x2", d => d.target.y ?? 0)
            .attr("y2", d => d.target.x ?? 0)
            .attr("stroke", "#555")
            .attr("stroke-width", 2);

        g.selectAll("circle")
            .data(root.descendants())
            .enter()
            .append("circle")
            .attr("cx", d => d.y ?? 0) // Swap x/y
            .attr("cy", d => d.x ?? 0)
            .attr("r", 10)
            .attr("fill", d => d.depth === 0 ? "gold" : d.data.nation === "Judah" ? "blue" : "red")
            .attr("stroke", "black")
            .attr("stroke-width", 2)
            .on("click", (_, d) => alert(`${d.data.name} reigned ${d.data.reign}`));

        g.selectAll("text")
            .data(root.descendants())
            .enter()
            .append("text")
            .attr("x", d => (d.y !== undefined ? d.y + 14 : 0)) // ✅ Ensure y is defined
            .attr("y", d => (d.x !== undefined ? d.x : 0)) // ✅ Ensure x is defined
            .text(d => d.data.name)
            .attr("font-size", "20px")
            .attr("fill", "#333");

        // ✅ Add Zoom & Pan functionality (Fixed TypeScript typing)
        const zoom: d3.ZoomBehavior<SVGSVGElement, unknown> = d3.zoom<SVGSVGElement, unknown>()
            .scaleExtent([0.5, 2])
            .on("zoom", (event) => {
                g.attr("transform", event.transform);
            });

        d3.select<SVGSVGElement, unknown>(svgRef.current).call(zoom);
    };

    return (
        <div>
            <h2>Lineage of Kings</h2>
            <h3></h3>
            <svg ref={svgRef}></svg>
        </div>
    );
};

export default LineageTree;