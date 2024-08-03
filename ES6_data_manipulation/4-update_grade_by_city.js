/* eslint-disable */

export default function updateGradeByCity(array, city, newGrades) {
    if (!Array.isArray(array)) {
        return [];
    }

    return array.map((student) => {
        if (student.location === city) {
            return {
                ...student,
                grade: newGrades.reduce((acc, grade) => grade.studentId === student.id ? grade.grade : acc, 'N/A'),
            };
        }
        return student;
    }).filter((student) => student.grade);
}
