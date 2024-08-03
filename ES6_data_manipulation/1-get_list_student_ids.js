/* eslint-disable */

export default function getStudentIds(array) {
    if (!Array.isArray(array)) {
        return [];
    }
    return array.map((student) => student.id);
}
