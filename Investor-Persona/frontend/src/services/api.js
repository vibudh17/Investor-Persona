const API_URL = "http://127.0.0.1:8000";

export async function analyzeNews(investorId, newsText) {

  const response = await fetch(`${API_URL}/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      investor_id: investorId,
      news: newsText
    })
  });

  return response.json();
}