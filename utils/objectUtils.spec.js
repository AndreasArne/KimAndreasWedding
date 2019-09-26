import ObjectUtils from './objectUtils.js'
import { exportAllDeclaration } from '@babel/types';

describe('Object Utils', () => {
    var objectUtils;
    
    beforeAll(() => {
        objectUtils = new ObjectUtils();
    })

    describe('getNested', () => {
        it('should return value if object path has length one', () => {
            const object = { '1': 'one' }
            const result = objectUtils.getNested(object, ['1'])

            expect(result).toEqual('one');
        })
        it('should return value if object path is longer than one', () => {
            const object = { '1': { '2': { '3': 'three'}}}
            const result = objectUtils.getNested(object, ['1', '2', '3'])
            
            expect(result).toEqual('three')
        })
        it('should return undefined if object path of length one does not exist', () => {
            const object = { 'four': 'one' }
            const result = objectUtils.getNested(object, ['five'])

            expect(result).toBeUndefined();
        })
        it('should return undefined if object path of length longer than one does not exist', () => {
            const object = { '1': { '2': { '3': 'three'}}}
            const result = objectUtils.getNested(object, ['1', '2', '4'])

            expect(result).toBeUndefined();
        })
    }) 
})