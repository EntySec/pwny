/*
 * MIT License
 *
 * Copyright (c) 2020-2023 EntySec
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#ifndef _API_H_
#define _API_H_

#include <tlv.h>
#include <c2.h>

#include <uthash/uthash.h>

#define TAB_API_CALL 1

enum api_call_statuses {
    API_CALL_QUIT,
    API_CALL_SUCCESS,
    API_CALL_FAIL,
    API_CALL_WAIT,
    API_CALL_NOT_IMPLEMENTED,
    API_CALL_USAGE_ERROR,
    API_CALL_RW_ERROR,
};

typedef tlv_pkt_t *(*api_t)(c2_t *);

typedef struct api_calls_table
{
    int tag;
    api_t handler;
    UT_hash_handle hh;
} api_calls_t;

tlv_pkt_t *api_craft_tlv_pkt(int);
tlv_pkt_t *api_call_make(api_calls_t **, c2_t *, int);

void api_calls_register(api_calls_t **);
void api_call_register(api_calls_t **, int, api_t);

void api_calls_free(api_calls_t *);

#endif /* _API_H_ */
