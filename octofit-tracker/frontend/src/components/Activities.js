import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://legendary-orbit-959wqj5xrp9fpqx6-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.type} - {activity.duration} mins</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;