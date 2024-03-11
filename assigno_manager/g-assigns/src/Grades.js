import React, { useState, useEffect } from 'react';
// import axios from 'axios';
import { Button } from 'primereact/button';
import { Card } from 'primereact/card';
import { units, grades } from './data';
import { Paginator } from 'primereact/paginator';

const url = 'http://localhost:8000/';

function Grades() {
    // Return: grades per unit
    // After going to set route, prompt for unit to show grade
    // Then fetch for grade info for select unit & render

  //   const [grades, setGrades] = useState([]);
    const [showGrades, setShowGrades] = useState(false);
    const [showUnits, setShowUnits] = useState(true);
  //   const [units, setUnits] = useState([]);
  //   const [currentUnitId, setCurrentUnitId] = useState(0);

  //   console.log(Card)

  //   useEffect(() => {
  //     (async () => {
  //         try{
  //             const full_url = `${url}units/`;
  //             const data = await axios.get(full_url);
  //             setUnits(data.data);
  //         } catch (err) {
  //             console.error(err);
  //         }
  //     })();
  // }, []);

  //   useEffect(() => {
  //       (async () => {
  //         if (currentUnitId !== 0) {
  //           // prevent from fetching first time (default id == 0)
  //           try {
  //             const full_url = `${url}grades/${currentUnitId}/`;
  //             const data = await axios.get(full_url);
  //             setGrades(data.data);
  //           } catch (err) {
  //             console.error(err);
  //           }
  //         }
  //       })();
  //   }, [currentUnitId]);


    const handleChooseUnit = (unitId) => {
      setShowUnits(false);
      // setCurrentUnitId(unitId);
      setShowGrades(true);
    }

  const exitUnitGrade = () => {
      setShowUnits(true);
  //     setCurrentUnitId(0);
      setShowGrades(false);
     }

    return (
      <div className="grades">
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
        {showGrades && (
          <div>
            {grades.map((grade) => (
              <Card title={grade.title} key={grade.id} className="grade-view">
                <p>
                  Grade: {grade.grade ? grade.grade : `unassigned`}{" "}
                  {grade.grade ? " / " : ""}
                  {grade.grade ? grade.maxPoints : ""}
                </p>
              </Card>
            ))}
            <Button label="Go back" onClick={exitUnitGrade} />
          </div>
        )}
      </div>
    );
}

export default Grades;