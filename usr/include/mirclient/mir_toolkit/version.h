/*
 * Copyright © 2014-2017 Canonical Ltd.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License version 3,
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#ifndef MIR_TOOLKIT_VERSION_H_
#define MIR_TOOLKIT_VERSION_H_

#include "mir_toolkit/mir_version_number.h"

/**
 * \addtogroup mir_toolkit
 * @{
 */

#define MIR_CLIENT_API_VERSION_MAJOR (0)
#define MIR_CLIENT_API_VERSION_MINOR (26)
#define MIR_CLIENT_API_VERSION_PATCH (3)

/**
 * The current version of the Mir client headers in use.
 * For example, to test for a feature introduced in Mir version 1.2.3 you would
 * write:
 *    #if defined(MIR_CLIENT_API_VERSION) && \
 *        MIR_CLIENT_API_VERSION >= MIR_VERSION_NUMBER(1,2,3)
 *
 */
#define MIR_CLIENT_API_VERSION MIR_VERSION_NUMBER(MIR_CLIENT_API_VERSION_MAJOR,\
                                                  MIR_CLIENT_API_VERSION_MINOR,\
                                                  MIR_CLIENT_API_VERSION_PATCH)

/* Deprecated. Do not update these. */
#define MIR_CLIENT_MAJOR_VERSION (3) /**< \deprecated */
#define MIR_CLIENT_MINOR_VERSION (5) /**< \deprecated */
#define MIR_CLIENT_MICRO_VERSION (0) /**< \deprecated */
#define MIR_CLIENT_VERSION \
    MIR_VERSION_NUMBER(MIR_CLIENT_MAJOR_VERSION, \
                       MIR_CLIENT_MINOR_VERSION, \
                       MIR_CLIENT_MICRO_VERSION)

/**@}*/

#endif /* MIR_TOOLKIT_VERSION_H_ */
