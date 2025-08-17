import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Job Tracker</h1>
        <p>Track your job applications and opportunities</p>
      </header>
      <main>
        <div className="container">
          <h2>Welcome to Job Tracker</h2>
          <p>Your comprehensive job application management system</p>
          <div className="features">
            <div className="feature">
              <h3>📋 Track Applications</h3>
              <p>Keep track of all your job applications</p>
            </div>
            <div className="feature">
              <h3>📊 Analytics</h3>
              <p>View insights and progress</p>
            </div>
            <div className="feature">
              <h3>🔔 Notifications</h3>
              <p>Stay updated on application status</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
