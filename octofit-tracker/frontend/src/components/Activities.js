import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    const baseUrl = 'https://legendary-orbit-959wqj5xrp9fpqx6-8000.app.github.dev/';
    const endpoint = 'api/activity/';
    const apiUrl = baseUrl + endpoint;

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Activity Type</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
