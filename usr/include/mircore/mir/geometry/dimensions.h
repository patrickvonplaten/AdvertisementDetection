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
 * Authored by: Alan Griffiths <alan@octopull.co.uk>
 */

#ifndef MIR_GEOMETRY_DIMENSIONS_H_
#define MIR_GEOMETRY_DIMENSIONS_H_

#include <cstdint>
#include <iosfwd>

namespace mir
{

/// Basic geometry types. Types for dimensions, displacements, etc.
/// and the operations that they support.
namespace geometry
{

namespace detail
{
template<typename Tag>
class IntWrapper
{
public:
    typedef int ValueType;

    constexpr IntWrapper() : value(0) {}
    constexpr IntWrapper(IntWrapper const& that) = default;
    IntWrapper& operator=(IntWrapper const& that) = default;

    template<typename AnyInteger>
    explicit constexpr IntWrapper(AnyInteger value) : value(static_cast<ValueType>(value)) {}

    constexpr uint32_t as_uint32_t() const  // TODO: Deprecate this later
    {
        return (uint32_t)value;
    }

    constexpr int as_int() const
    {
        return value;
    }

private:
    ValueType value;
};

template<typename Tag>
std::ostream& operator<<(std::ostream& out, IntWrapper<Tag> const& value)
{
    out << value.as_int();
    return out;
}

template<typename Tag>
inline constexpr bool operator == (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() == rhs.as_int();
}

template<typename Tag>
inline constexpr bool operator != (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() != rhs.as_int();
}

template<typename Tag>
inline constexpr bool operator <= (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() <= rhs.as_int();
}

template<typename Tag>
inline constexpr bool operator >= (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() >= rhs.as_int();
}

template<typename Tag>
inline constexpr bool operator < (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() < rhs.as_int();
}

template<typename Tag>
inline constexpr bool operator > (IntWrapper<Tag> const& lhs, IntWrapper<Tag> const& rhs)
{
    return lhs.as_int() > rhs.as_int();
}
} // namespace detail

typedef detail::IntWrapper<struct WidthTag> Width;
typedef detail::IntWrapper<struct HeightTag> Height;
// Just to be clear, mir::geometry::Stride is the stride of the buffer in bytes
typedef detail::IntWrapper<struct StrideTag> Stride;

typedef detail::IntWrapper<struct XTag> X;
typedef detail::IntWrapper<struct YTag> Y;
typedef detail::IntWrapper<struct DeltaXTag> DeltaX;
typedef detail::IntWrapper<struct DeltaYTag> DeltaY;

// Adding deltas is fine
inline constexpr DeltaX operator+(DeltaX lhs, DeltaX rhs) { return DeltaX(lhs.as_int() + rhs.as_int()); }
inline constexpr DeltaY operator+(DeltaY lhs, DeltaY rhs) { return DeltaY(lhs.as_int() + rhs.as_int()); }
inline constexpr DeltaX operator-(DeltaX lhs, DeltaX rhs) { return DeltaX(lhs.as_int() - rhs.as_int()); }
inline constexpr DeltaY operator-(DeltaY lhs, DeltaY rhs) { return DeltaY(lhs.as_int() - rhs.as_int()); }

// Adding deltas to co-ordinates is fine
inline constexpr X operator+(X lhs, DeltaX rhs) { return X(lhs.as_int() + rhs.as_int()); }
inline constexpr Y operator+(Y lhs, DeltaY rhs) { return Y(lhs.as_int() + rhs.as_int()); }
inline constexpr X operator-(X lhs, DeltaX rhs) { return X(lhs.as_int() - rhs.as_int()); }
inline constexpr Y operator-(Y lhs, DeltaY rhs) { return Y(lhs.as_int() - rhs.as_int()); }
inline X& operator+=(X& lhs, DeltaX rhs) { return lhs = X(lhs.as_int() + rhs.as_int()); }
inline Y& operator+=(Y& lhs, DeltaY rhs) { return lhs = Y(lhs.as_int() + rhs.as_int()); }
inline X& operator-=(X& lhs, DeltaX rhs) { return lhs = X(lhs.as_int() - rhs.as_int()); }
inline Y& operator-=(Y& lhs, DeltaY rhs) { return lhs = Y(lhs.as_int() - rhs.as_int()); }

// Adding deltas to Width and Height is fine
inline constexpr Width operator+(Width lhs, DeltaX rhs) { return Width(lhs.as_int() + rhs.as_int()); }
inline constexpr Height operator+(Height lhs, DeltaY rhs) { return Height(lhs.as_int() + rhs.as_int()); }
inline constexpr Width operator-(Width lhs, DeltaX rhs) { return Width(lhs.as_int() - rhs.as_int()); }
inline constexpr Height operator-(Height lhs, DeltaY rhs) { return Height(lhs.as_int() - rhs.as_int()); }

// Subtracting coordinates is fine
inline constexpr DeltaX operator-(X lhs, X rhs) { return DeltaX(lhs.as_int() - rhs.as_int()); }
inline constexpr DeltaY operator-(Y lhs, Y rhs) { return DeltaY(lhs.as_int() - rhs.as_int()); }

//Subtracting Width and Height is fine
inline constexpr DeltaX operator-(Width lhs, Width rhs) { return DeltaX(lhs.as_int() - rhs.as_int()); }
inline constexpr DeltaY operator-(Height lhs, Height rhs) { return DeltaY(lhs.as_int() - rhs.as_int()); }

// Multiplying by a scalar value is fine
template<typename Scalar>
inline constexpr Width operator*(Scalar scale, Width const& w) { return Width{scale*w.as_int()}; }
template<typename Scalar>
inline constexpr Height operator*(Scalar scale, Height const& h) { return Height{scale*h.as_int()}; }
template<typename Scalar>
inline constexpr DeltaX operator*(Scalar scale, DeltaX const& dx) { return DeltaX{scale*dx.as_int()}; }
template<typename Scalar>
inline constexpr DeltaY operator*(Scalar scale, DeltaY const& dy) { return DeltaY{scale*dy.as_int()}; }
template<typename Scalar>
inline constexpr Width operator*(Width const& w, Scalar scale) { return scale*w; }
template<typename Scalar>
inline constexpr Height operator*(Height const& h, Scalar scale) { return scale*h; }
template<typename Scalar>
inline constexpr DeltaX operator*(DeltaX const& dx, Scalar scale) { return scale*dx; }
template<typename Scalar>
inline constexpr DeltaY operator*(DeltaY const& dy, Scalar scale) { return scale*dy; }

template<typename Target, typename Source>
inline constexpr Target dim_cast(Source s) { return Target(s.as_int()); }
}
}

#endif /* MIR_GEOMETRY_DIMENSIONS_H_ */
