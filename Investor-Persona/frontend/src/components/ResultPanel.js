import React from "react";

function ResultPanel({ result }) {

  if (!result) return null;

  return (
    <div style={{marginTop: "30px"}}>

      <h2>AI Result</h2>

      <p><b>Persona:</b> {result.persona}</p>

      <p><b>News Category:</b> {result.news_category}</p>

      <p><b>Recommendation:</b> {result.recommendation}</p>

      <p><b>Explanation:</b> {result.explanation}</p>

    </div>
  );
}

export default ResultPanel;