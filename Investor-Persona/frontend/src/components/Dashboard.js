import React, { useState } from "react";
import NewsList from "./NewsList";
import ResultPanel from "./ResultPanel";
import { analyzeNews } from "../services/api";

function Dashboard() {

  const [result, setResult] = useState(null);

  async function handleNewsClick(news) {

    const response = await analyzeNews(1, news);

    setResult(response);
  }

  return (
    <div style={{padding: "40px"}}>

      <h1>Investor AI Dashboard</h1>

      <NewsList onSelect={handleNewsClick} />

      <ResultPanel result={result} />

    </div>
  );
}

export default Dashboard;