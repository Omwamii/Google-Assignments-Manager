import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const url = 'http://localhost:8000/';

function Notifs() {
    // could add prop for id of course to fetch
    const [notifs, setNotifs] = useState([]);
    const [showUnits, setShowUnits] = useState(true);
    const [units, setUnits] = useState([]);
    const [currentUnitId, setCurrentUnitId] = useState(0);
    
    useEffect(() => {
      (async () => {
          try{
              const full_url = `${url}units/`
              const data = await axios.get(full_url);
              setUnits(data.data);
              console.log(data.data) // validate data
          } catch (err) {
              console.error(err);
          }
      })();
  }, []);

    useEffect(() => {
        (async () => {
            try{
                const full_url = `${url}notifications/${currentUnitId}/`
                const data = await axios.get(full_url);
                setNotifs(data.data);
                console.log(data.data) // validate data
            } catch (err) {
                console.error(err);
            }
        })();
    }, [currentUnitId]);

    const handleChooseUnit = (unitId) => {
      setShowUnits(false);
      setCurrentUnitId(unitId);
    }

    return (
      <div className="notifications">
        <div className="units">
          {showUnits &&
            units.map((unit) => (
              <button
                key={unit.id}
                onClick={() => handleChooseUnit(unit.id)}
                type="button"
                className="btn btn-primary btn-lg btn-block"
              >
                {unit.name}
              </button>
            ))}
        </div>
        {notifs &&
          notifs.map((notif) => (
            <div
              key={notif.id}
              className="card border-info mb-3"
              style={{ maxWidth: "18rem" }}
            >
              <div className="card-header">{notif.time}</div>
              <div className="card-body text-info">
                {/* <h5 class="card-title">Info card title</h5> */}
                <p className="card-text">{notif.text}</p>
              </div>
              {/* <div className="card-footer">
          <small className="text-muted">{notif.time}</small>
          </div> */}
            </div>
          ))}
      </div>
    );
}

export default Notifs;