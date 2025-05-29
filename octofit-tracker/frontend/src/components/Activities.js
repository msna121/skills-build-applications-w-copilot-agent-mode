import React, { useEffect, useState } from 'react';

// Define the codespace Django REST API endpoint suffix for Activities
const ACTIVITIES_API_URL = 'https://legendary-orbit-959wqj5xrp9fpqx6-8000.app.github.dev/api/activity/';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(ACTIVITIES_API_URL)
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
