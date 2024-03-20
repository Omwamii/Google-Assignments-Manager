import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { FileUpload } from 'primereact/fileupload';
import { ProgressSpinner } from 'primereact/progressspinner';
import { ArrowLeft } from 'react-bootstrap-icons';
import { Toast } from 'primereact/toast';
import Navbar from './Navbar';
import PendingAssignmentsCache from './PendingCache';


const url = 'http://localhost:8000/';

function Home() {
  // Return: pending assignments
  // Add button to view submitted work in classroom if user had submitted some work?

  const [isLoading, setIsLoading] = useState(true);
  const [pendingWork, setPendingWork] = useState([]);
  const [showPendingWork, setShowPendingWork] = useState(false);
  const [currentWorkId, setCurrentWorkId] = useState(0);
  const [showCurrentWork, setShowCurrentWork] = useState(false);
  const [currentWork, setCurrentWork] = useState([]);
  const [currentUnitId, setCurrentUnitId] = useState(0);
  const toast = useRef(null);
  
  const Cache = new PendingAssignmentsCache();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const fullUrl = `${url}assignments/`;
        const response = await axios.get(fullUrl);
        Cache.saveData(response.data) // save response data to cache
        setPendingWork(response.data);
        setIsLoading(false);
        setShowPendingWork(true);
      } catch (error) {
        console.error(error);
      }
    };
    if (Cache.hasExpired()) {
      Cache.deleteData()
      fetchData();
    } else {
      // cache not expired
      setPendingWork(Cache.getData())
      setIsLoading(false);
      setShowPendingWork(true);
    }
  }, []);

  // fetch assignment details
  useEffect(() => {
    (async () => {
      if (currentWorkId !== 0 && currentUnitId !== 0) {
        // prevent from fetching first time (default id == 0)
        // add load before loading current work (might have previous data)
        try {
          const full_url = `${url}assignment/${currentUnitId}/${currentWorkId}/`;
          const data = await axios.get(full_url);
          setCurrentWork(data.data); 
          setIsLoading(false); // data is ready
        } catch (err) {
          console.error(err);
        }
      }
    })();
  }, [currentWorkId, currentUnitId]);

  const viewWork = (workId, courseId) => {
    // go to assignment page
    setIsLoading(true);
    setCurrentWorkId(workId);
    setCurrentUnitId(courseId);
    setShowPendingWork(false);
    setShowCurrentWork(true);
  };

  const exitView = () => {
    // exit from viewing assignment
    setCurrentWorkId(0);
    setCurrentUnitId(0);
    setShowPendingWork(true);
    setShowCurrentWork(false);
    setCurrentWork([]);
  }

  const markAsDone = async (work_id, unit_id) => {
    try {
      const full_url = `${url}mark-done/${unit_id}/${work_id}/`;
      const data = await axios.post(full_url);
      if (data.data.error) {
        toast.current.show({ severity: 'error', summary: 'Error', detail: data.data.message });
      } else {
        toast.current.show({ severity: 'success', summary: 'Info', detail: data.data.message });
        toast.current.show({ severity: 'info', summary: 'Info', detail: 'It might take a while for the work to be removed due to caching' });
      }
    } catch (err) {
      console.error(err);
      toast.current.show({ severity: 'error', summary: 'Error', detail: 'Error! could not mark work as done' });
    }
  }

  const handleUploaded = () => {
    // toast.current.show({ severity: 'info', summary: 'Info', detail: 'Message Content' });
    console.log('Has been uploaded');
  }

  if (isLoading) {
    return (
      <div>
        <Navbar />
        <div className="app-content">
          <ProgressSpinner />
        </div>
      </div>
    );
  }
  return (
    <div>
      <Navbar />
      <Toast ref={toast} position='top-center'/>
      {showPendingWork && (
        <div className="pending app-content">
          {pendingWork.length > 0 ? pendingWork.map((pending) => (
            <div className="card assignment" key={pending.id}>
              <div className="card-body">
                <h5 className="card-title">{pending.unit}</h5>
                <p className="card-text">
                  {pending.title} {pending.points && `(${pending.points} pts)`}
                </p>
                <div className="pending-work-btns">
                  <button
                    type="button"
                    className="btn btn-primary"
                    onClick={() => viewWork(pending.id, pending.courseId)}
                  >
                    View work
                  </button>
                  <button type="button" className="btn btn-primary" id="view">
                    <a
                      href={pending.classLink}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      View in classroom
                    </a>
                  </button>
                  {pending.dueTime === " No due time" || pending.dueTime.split(" ")[1] === "passed" ? (
                    <button
                      type="button"
                      className="btn btn-secondary"
                      id="mark-done"
                      onClick={() => markAsDone(pending.id, pending.courseId)}
                    >
                      Mark as done
                    </button>
                  ) : (
                    ""
                  )}
                </div>
              </div>
              <div className="card-footer">
                <small className="text-muted">Due in: {pending.dueTime}</small>
              </div>
            </div>
          )) : (<h1 className='disp-text'>{`No pending work  :)`}</h1>)}
        </div>
      )}
      {showCurrentWork && (
          <div className="assignment-view app-content">
            <ArrowLeft
              color="crimson"
              size={65}
              onClick={exitView}
              className="arrow"
            />
            <div className="card assignment">
              <div className="card-header">{currentWork.title}</div>
              <div className="card-body">
                <p className="card-text">{currentWork.description}</p>
              </div>
              <div className="card-footer">
                <small className="text-muted">Due in: {currentWork.time}</small>
              </div>
            </div>
            <div className="card" id="files">
              <div className="card-header">Files</div>
              <div className="card-body">
                <FileUpload
                  name="file"
                  url={`${url}submit-assignment/${currentUnitId}/${currentWorkId}/`}
                  multiple
                  accept="*/*"
                  onUpload={handleUploaded}
                  maxFileSize={1000000}
                  emptyTemplate={
                    <p className="m-0">
                      Drag and drop files to here to upload.
                    </p>
                  }
                />
              </div>
              <div className="card-footer">
                <small className="text-muted">
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