export default class GuestsService {
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
        return this.makeRequest('POST', 'http://localhost:8000/get_party', 'json', JSON.stringify({"id":hash}))
    }

    putParty(party) {
        return this.makeRequest('PUT', 'http://localhost:8000/update_party', 'json', JSON.stringify(party))
    }
}