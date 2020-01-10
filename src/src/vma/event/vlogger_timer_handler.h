/*
 * Copyright (c) 2001-2016 Mellanox Technologies, Ltd. All rights reserved.
 *
 * This software is available to you under a choice of one of two
 * licenses.  You may choose to be licensed under the terms of the GNU
 * General Public License (GPL) Version 2, available from the file
 * COPYING in the main directory of this source tree, or the
 * BSD license below:
 *
 *     Redistribution and use in source and binary forms, with or
 *     without modification, are permitted provided that the following
 *     conditions are met:
 *
 *      - Redistributions of source code must retain the above
 *        copyright notice, this list of conditions and the following
 *        disclaimer.
 *
 *      - Redistributions in binary form must reproduce the above
 *        copyright notice, this list of conditions and the following
 *        disclaimer in the documentation and/or other materials
 *        provided with the distribution.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */


#ifndef VLOGGER_TIMER_HANDLER_H
#define VLOGGER_TIMER_HANDLER_H

#include "timer_handler.h"

#define UPDATE_VLOGGER_LEVELS_INTERVAL	100

class vlogger_timer_handler : public timer_handler
{
public:
	vlogger_timer_handler();
	~vlogger_timer_handler();
private:
	void handle_timer_expired(void* user_data);
	
	void*	m_timer_handle;
};

extern vlogger_timer_handler* g_p_vlogger_timer_handler;

#endif /*VLOGGER_TIMER_HANDLER_H*/
