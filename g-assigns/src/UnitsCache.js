// cache units to prevent unnecessary calls to backend

class UnitsCache {
    constructor() {}

    hasExpired() {
        // check if an object has reached its expiry time in cache
        const expiryTimeString = JSON.parse(localStorage.getItem('units_expiry'))
        const expiryTime = (new Date(expiryTimeString)).getTime()
        const currentTime = (new Date()).getTime()
        if (!expiryTime || currentTime > expiryTime) {
            return true // data has expired
        }
        return false; // not yet expired
    }

    saveData(data){
        // save data to local storage
        localStorage.setItem('units_data', JSON.stringify(data))
        const currentTime = new Date()
        // set the expiry time to 15 minutes? (in milliseconds)
        const expiryTime = new Date(currentTime.getTime() + (15 * 60 * 1000));
        localStorage.setItem('units_expiry', JSON.stringify(expiryTime))
    }

    deleteData() {
        // delete data from localstorage
        localStorage.removeItem('units_data')
        localStorage.removeItem('units_expiry')
    }

    getData() {
        return JSON.parse(localStorage.getItem('units_data'));
    }
}

export default UnitsCache;