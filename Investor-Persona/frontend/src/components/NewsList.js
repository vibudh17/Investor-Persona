import React from "react";

const newsData = [
  "Gold prices increase due to inflation",
  "Crypto market crashes suddenly",
  "Government bonds becoming stable investment",
  "Tech stocks rally in the market"
];

function NewsList({ onSelect }) {

  return (
    <div>
      <h2>News</h2>

      {newsData.map((news, index) => (
        <div key={index} style={{marginBottom: "10px"}}>

          <button onClick={() => onSelect(news)}>
            Analyze
          </button>

          {" "} {news}

        </div>
      ))}

    </div>
  );
}

export default NewsList;