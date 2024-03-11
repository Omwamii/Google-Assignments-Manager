import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import { units, notifs } from './data';
import { Fieldset } from 'primereact/fieldset';
import { Button } from 'primereact/button';

const url = 'http://localhost:8000/';

function Notifs() {
    // Fetch notifications from classroom & display
    // prompts for unit to show notifications, fetch& display
    
    // const [notifs, setNotifs] = useState([]);
    const [showUnits, setShowUnits] = useState(true);
    const [showNotifs, setShowNotifs] = useState(false);
    // const [units, setUnits] = useState([]);
    // const [currentUnitId, setCurrentUnitId] = useState(0);
    
  //   useEffect(() => {
  //     (async () => {
  //         try{
  //             const full_url = `${url}units/`
  //             const data = await axios.get(full_url);
  //             setUnits(data.data);
  //             console.log(data.data) // validate data
  //         } catch (err) {
  //             console.error(err);
  //         }
  //     })();
  // }, []);

  //   useEffect(() => {
  //       (async () => {
  //           try{
  //               const full_url = `${url}notifications/${currentUnitId}/`
  //               const data = await axios.get(full_url);
  //               setNotifs(data.data);
  //               console.log(data.data) // validate data
  //           } catch (err) {
  //               console.error(err);
  //           }
  //       })();
  //   }, [currentUnitId]);

    const handleChooseUnit = (unitId) => {
      setShowUnits(false);
      setShowNotifs(true);
      // setCurrentUnitId(unitId);
    };

    const exitView = () => {
      setShowUnits(true)
      setShowNotifs(false)
    };
    return (
      <div className="notifications">
        <div className="units">
          {showUnits &&
            units.map((unit) => (
              <Button
              className='unit-btn'
                label={unit.name}
                key={unit.id}
                onClick={() => handleChooseUnit(unit.id)}
              />
            ))}
        </div>
        {showNotifs &&
          notifs.map((notif) => (
            <div className="card" id="notifs">
              <Fieldset legend={notif.time} key={notif.id}>
                <p className="mt-5">{notif.text}</p>
              </Fieldset>
            </div>
          ))}
      </div>
    );
}

export default Notifs;