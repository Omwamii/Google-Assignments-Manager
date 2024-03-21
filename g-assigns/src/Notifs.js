import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import { Fieldset } from 'primereact/fieldset';
import { Button } from 'primereact/button';
import Navbar from './Navbar';
import { ArrowLeft } from 'react-bootstrap-icons';
import { ProgressSpinner } from 'primereact/progressspinner';

import UnitsCache from './UnitsCache';

const url = 'http://localhost:8000/';

function Notifs() {
    // Fetch notifications from classroom & display
    // prompts for unit to show notifications, fetch& display
    
    const [notifs, setNotifs] = useState([]);
    const [isLoading, setIsLoading] = useState(true)
    const [showUnits, setShowUnits] = useState(true);
    const [showNotifs, setShowNotifs] = useState(false);
    const [units, setUnits] = useState([]);
    const [currentUnitId, setCurrentUnitId] = useState(0);
    
    const Cache = new UnitsCache();

    useEffect(() => {
      const fetchData = async () => {
        try {
          const fullUrl = `${url}units/`;
          const response = await axios.get(fullUrl);
          Cache.saveData(response.data) // save response data to cache
          setUnits(response.data);
          setIsLoading(false);
          setShowUnits(true);
        } catch (error) {
          console.error(error);
        }
      };
      if (Cache.hasExpired()) {
        Cache.deleteData()
        fetchData();
      } else {
        setUnits(Cache.getData())
        setIsLoading(false);
        setShowUnits(true);
      }
  }, []);

    useEffect(() => {
        (async () => {
          if (currentUnitId !== 0) {
            // avoid fetching first time
            try{
              const full_url = `${url}notifications/${currentUnitId}/`
              const data = await axios.get(full_url);
              setNotifs(data.data);
              setIsLoading(false);
          } catch (err) {
              console.error(err);
          }
          }
        })();
    }, [currentUnitId]);

    const handleChooseUnit = (unitId) => {
      setIsLoading(true);
      setShowUnits(false);
      setShowNotifs(true);
      setCurrentUnitId(unitId);
    };

    const exitView = () => {
      setShowUnits(true)
      setShowNotifs(false)
    };

    if (isLoading) {
      return (
        <div>
          <Navbar />
          <div className='app-content'>
            <ProgressSpinner />
          </div>
        </div>
      )
    }
    return (
      <div>
        <Navbar />
        <div className="notifications app-content">
          <div className="units">
            {showUnits &&
              units.map((unit) => (
                <Button
                  className="unit-btn"
                  label={unit.name}
                  key={unit.id}
                  onClick={() => handleChooseUnit(unit.id)}
                />
              ))}
          </div>
          {showNotifs && (
            <div>
            <ArrowLeft color="crimson" size={65} onClick={exitView}  className='arrow'/>
            {notifs.length > 0 ? (notifs.map((notif) => (
              <div className="card" id="notifs" key={notif.id}>
                <Fieldset legend={notif.time} key={notif.id}>
                  <p className="mt-5">{notif.text}</p>
                </Fieldset>
              </div>
            ))) : (<h1 className='disp-text'>No notifications yet</h1>)}
            </div>
          )}
        </div>
      </div>
    );
}

export default Notifs;