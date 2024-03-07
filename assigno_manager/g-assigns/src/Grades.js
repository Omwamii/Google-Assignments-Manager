import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Grades.css';

function Grades() {
    const [grades, setGrades] = useState(null);
    const [showUnits, setShowUnits] = useState(false);
    const [units, setUnits] = useState([]);
    const [currentUnitId, setCurrentUnitId] = useState(0);

    useEffect(() => {
        (async () => {
            try{
                const url = 'http://localhost:8000/grades/'
                const data = await axios.get(url);
                setGrades(data.data);
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
      <div className="grades">
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
        {grades && (
          <ul>
            {grades.map((grade) => (
              <li key={grade.title}>
                {grade.title}: {grade.grade} / {grade.maxPoints}
              </li> // Assuming each grade has an 'id' property
            ))}
          </ul>
        )}
      </div>
    );
}

export default Grades;