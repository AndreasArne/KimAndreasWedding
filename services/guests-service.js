export default class GuestsService {
    constructor() {
    }

    makeRequest(method, url, responseType) {
        const request = new XMLHttpRequest();

        return new Promise((resolve, reject) => {
            request.onreadystatechange = () => {
                if (request.readyState !== 4) return

                if (request.status >= 200 && request.status < 300) {
                    resolve(request.response);
                } else {
                    reject({
                        status: request.status,
                        statusText: request.statusText
                    });
                }
            }

            request.open(method, url)
            request.responseType = responseType
            request.send()
        });
    }

    getMockGuests(hash) {
        return this.makeRequest('GET', 'http://localhost:9000/guests?hash=' + hash, 'json')
    }
}