/* eslint-disable */

export default function hasArrayValues(set, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (!set.has(arr[i])) {
            return false;
        }
    }
    return true;
}
