import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button } from 'primereact/button';
import { Card } from 'primereact/card';
import { ArrowLeft } from 'react-bootstrap-icons';
import { ProgressSpinner } from 'primereact/progressspinner';

import Navbar from './Navbar';
import UnitsCache from './UnitsCache';

const url = 'http://localhost:8000/';

function Grades() {
    // Return: grades per unit
    // After going to set route, prompt for unit to show grade
    // Then fetch for grade info for select unit & render

    const [grades, setGrades] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [showGrades, setShowGrades] = useState(false);
    const [showUnits, setShowUnits] = useState(false);
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
            // prevent from fetching first time (default id == 0)
            try {
              const full_url = `${url}grades/${currentUnitId}/`;
              const data = await axios.get(full_url);
              setGrades(data.data);
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
      setCurrentUnitId(unitId);
      setShowGrades(true);
    }

  const exitUnitGrade = () => {
      setShowUnits(true);
      setCurrentUnitId(0);
      setShowGrades(false);
     }

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
        <div className="grades">
        <div className="units app-content">
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
          <ArrowLeft className="arrow" color="crimson" size={65} onClick={exitUnitGrade} />
            {grades.length > 0 ? (grades.map((grade) => (
              <Card title={grade.title} key={grade.id} className="grade-view">
                <p>
                  Grade: {grade.grade ? grade.grade : `unassigned`}{" "}
                  {grade.grade ? " / " : ""}
                  {grade.grade ? grade.maxPoints : ""}
                </p>
              </Card>
            ))) : (<h1 className='disp-text'>No work posted yet</h1>)}
          </div>
        )}
      </div>
      </div>
    );
}

export default Grades;