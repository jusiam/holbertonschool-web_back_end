/* eslint-disable */

export default function getStudentsByLocation(array, location) {
    if (!Array.isArray(array)) {
        return [];
    }
    return array.filter((student) => student.location === location);
}
