/* eslint-disable */

export default function getStudentIdsSum(students) {
    if (!Array.isArray(students)) {
        return [];
    }
    return students.map((student) => student.id).reduce((prev, curr) => prev + curr, 0);
}
