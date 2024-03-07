import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const url = 'http://localhost:8000/';

function Home() {
  const [pendingWork, setPendingWork] = useState([]);
  const [showPendingWork, setShowPendingWork] = useState(true);
  const [currentWorkId, setCurrentWorkId] = useState(0);
  const [currentWork, setCurrentWork] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const fullUrl = `${url}assignments/`;
        const data = await axios.get(fullUrl);
        setPendingWork(data.data);
        console.log(data.data); // validate data
      } catch (err) {
        console.error(err);
      }
    })();
  }, [showPendingWork]);

  // fetch assignment details
  useEffect(() => {
    (async () => {
      if (currentWorkId !== 0) {
        // prevent from fetching first time (default id == 0)
        try {
          const full_url = `${url}assignment/${currentWorkId}/`;
          const data = await axios.get(full_url);
          setCurrentWork(data.data);
          console.log(data.data); // validate data
        } catch (err) {
          console.error(err);
        }
      }
    })();
  }, [currentWorkId]);

  const viewWork = (workId) => {
    setShowPendingWork(false);
    setCurrentWorkId(workId);
  };

  return (
    <div className="card-deck">
      {showPendingWork &&
        pendingWork.map((pending) => (
          <div class="card" key={pending.id}>
            <div class="card-body">
              <h5 class="card-title">{pending.unit}</h5>
              <p class="card-text">{pending.title}</p>
              <div className="pending-work-btns">
                <button
                  type="button"
                  class="btn btn-primary"
                  onClick={() => viewWork(pending.id)}
                >
                  View work
                </button>
                <button type="button" class="btn btn-primary">
                  View in classroom
                </button>
              </div>
            </div>
            <div class="card-footer">
              <small class="text-muted">Last updated 3 mins ago</small>
            </div>
          </div>
        ))}
      {currentWork && (
        <div className="card-deck">
          <div className="card">
            <div className="card-header">{currentWork.title}</div>
            <div class="card-body">
              <p class="card-text">{currentWork.description}</p>
            </div>
            <div class="card-footer">
              <small class="text-muted">Due on {currentWork.dueTime}</small>
            </div>
          </div>
          <div class="card">
            <div className="card-header">Files</div>
            <div className='files'>
                files to submit go here
            </div>
            <div class="card-body">
              <button type="button" class="btn btn-primary">
                Add files
              </button>
            </div>
            <div class="card-footer">
              <small class="text-muted">
                Add or remove files for submission
              </small>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Home;