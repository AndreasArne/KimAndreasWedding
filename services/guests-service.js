export default class GuestsService {
    constructor() {
        this.apiUrl = API_URL || 'https://bröllop.arnesson.dev/api';
    }

    makeRequest(method, url, responseType, data) {
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
            if (['PUT', 'POST'].includes(method)) request.setRequestHeader("Content-Type", "application/json")
            data ? request.send(data) : request.send()
        });
    }

    getParty(hash) {
        return this.makeRequest('POST', `${this.apiUrl}/get_party`, 'json', JSON.stringify({"id":hash}))
    }

    putParty(party) {
        return this.makeRequest('PUT', `${this.apiUrl}/update_party`, 'json', JSON.stringify(party))
    }
}