/*
 * Copyright © 2012, 2016 Canonical Ltd.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License version 3,
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 *
 * Authored by: Alexandros Frantzis <alexandros.frantzis@canonical.com>
 */

#ifndef MIR_GEOMETRY_DISPLACEMENT_H_
#define MIR_GEOMETRY_DISPLACEMENT_H_

#include "mir/geometry/dimensions.h"
#include "mir/geometry/point.h"

#include <iosfwd>

namespace mir
{
namespace geometry
{

struct Displacement
{
    constexpr Displacement() {}
    constexpr Displacement(Displacement const&) = default;
    Displacement& operator=(Displacement const&) = default;

    template<typename DeltaXType, typename DeltaYType>
    constexpr Displacement(DeltaXType&& dx, DeltaYType&& dy) : dx{dx}, dy{dy} {}

    long long length_squared() const
    {
        long long x = dx.as_int(), y = dy.as_int();
        return x * x + y * y;
    }

    DeltaX dx;
    DeltaY dy;
};

inline constexpr bool operator==(Displacement const& lhs, Displacement const& rhs)
{
    return lhs.dx == rhs.dx && lhs.dy == rhs.dy;
}

inline constexpr bool operator!=(Displacement const& lhs, Displacement const& rhs)
{
    return lhs.dx != rhs.dx || lhs.dy != rhs.dy;
}

std::ostream& operator<<(std::ostream& out, Displacement const& value);

inline constexpr Displacement operator+(Displacement const& lhs, Displacement const& rhs)
{
    return Displacement{lhs.dx + rhs.dx, lhs.dy + rhs.dy};
}

inline constexpr Displacement operator-(Displacement const& lhs, Displacement const& rhs)
{
    return Displacement{lhs.dx - rhs.dx, lhs.dy - rhs.dy};
}

inline constexpr Point operator+(Point const& lhs, Displacement const& rhs)
{
    return Point{lhs.x + rhs.dx, lhs.y + rhs.dy};
}

inline constexpr Point operator+(Displacement const& lhs, Point const& rhs)
{
    return Point{rhs.x + lhs.dx, rhs.y + lhs.dy};
}

inline constexpr Point operator-(Point const& lhs, Displacement const& rhs)
{
    return Point{lhs.x - rhs.dx, lhs.y - rhs.dy};
}

inline constexpr Displacement operator-(Point const& lhs, Point const& rhs)
{
    return Displacement{lhs.x - rhs.x, lhs.y - rhs.y};
}

inline bool operator<(Displacement const& lhs, Displacement const& rhs)
{
    return lhs.length_squared() < rhs.length_squared();
}

template<typename Scalar>
inline constexpr Displacement operator*(Scalar scale, Displacement const& disp)
{
    return Displacement{scale*disp.dx, scale*disp.dy};
}

template<typename Scalar>
inline constexpr Displacement operator*(Displacement const& disp, Scalar scale)
{
    return scale*disp;
}

#ifdef MIR_GEOMETRY_SIZE_H_
inline constexpr Displacement as_displacement(Size const& size)
{
    return Displacement{size.width.as_int(), size.height.as_int()};
}

inline constexpr Size as_size(Displacement const& disp)
{
    return Size{disp.dx.as_int(), disp.dy.as_int()};
}
#endif
}
}

#endif /* MIR_GEOMETRY_DISPLACEMENT_H_ */
