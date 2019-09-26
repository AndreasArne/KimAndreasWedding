export default class ObjectUtils {
    getNested(obj, pathArr) {
        return pathArr.reduce((acc, key) => {
            return (acc && acc[key] != undefined) ? acc[key] : undefined
        }, obj);
    }
}